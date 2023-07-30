import argparse
import gzip
import os
import shutil
import sys
import threading

# get the command-line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output',nargs=1,required=True,help="select backup folder")
    parser.add_argument('-i','--input',nargs='+',required=True,help="select file to be backed up")
    parser.add_argument('-c','--compress',nargs=1,type=int,help='gzip byte threshold (default is 2048kb)',default=[2048000])
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    return parser.parse_args()
  
# return the size of the input if there were new changes made to it
def check_difference(input, output):
    input_file_descriptor = os.stat(input)
    try:
        output_mtime = os.stat(output).st_mtime #mtime = time files were last modified
    except FileNotFoundError:
        try:
            output_mtime = os.stat(output+'.gz').st_mtime
        except FileNotFoundError:
            output_mtime = 0

    return input_file_descriptor.st_size if (
        input_file_descriptor.st_mtime - output_mtime
    ) else False

# copy file from source to output as ZIP
def transfer_file(input, output, compress):
    try:
        if compress:
            with gzip.open(output+'.gz','wb') as output_file:
                with open(input, 'rb') as input_file:
                    output_file.writelines(input_file)
            print(f"compress {input}")
        else:
            # apparently copy2 removes the rounds mtime to seconds
            shutil.copy2(input,output)
            print(f"copied {input}")
    except FileNotFoundError:
        os.makedirs(os.path.dirname(output))
        transfer_file(input, output, compress)


# thread for syncing files
def sync_file_thread(input,output,compress):
    size = check_difference(input, output)
    if size:
        thread = threading.Thread(target=transfer_file, args=(input,output,size>compress))
        thread.start()
        return thread

# sync files
def sync_file(input, output, compress):
    size = check_difference(input, output)
    if size:
        transfer_file(input, output, size > compress)

# sync root with output
def sync_root(root, arg):
    output = arg.output[0]
    compress = arg.compress[0]
    threads = []
    for path, _, files in os.walk(root):
        for file in files:
            file = path + '/' + file
            threads.append(
                sync_file_thread(file, output + file, compress)
            )
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    arg = parse_args()
    for root in arg.source:
        sync_root(root, arg)
    print("done")
