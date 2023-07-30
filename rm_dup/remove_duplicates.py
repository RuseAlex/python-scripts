import os
import hashlib

def hash_file(filename):
    FILE_BLOCK_SIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        buffer = file.read()
        while (len(buffer) > 0):
            hasher.update(buffer)
            buffer = file.read(FILE_BLOCK_SIZE)
    return hasher.hexdigest()

if __name__ == "__main__":
    hashMap = {}
    deletedFiles = []
    filelist = [obj for obj in os.listdir() if os.path.isfile(obj)]
    for file in filelist:
        key = hash_file(file)
        if key in hashMap.keys():
            deletedFiles.append(file)
            os.remove(file)
        else:
            hashMap[key] = file
    
    if len(deletedFiles) != 0:
        print(f'deleted {len(deletedFiles)} files')
    else:
        print("no duplicate files found")