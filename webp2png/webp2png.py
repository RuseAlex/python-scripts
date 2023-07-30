from PIL import Image
import os
import argparse
import sys

def convert(filename):
    img = Image.open(f"{filename}.webp").convert("RGB")
    img.save(f"{filename}.png", "png")
    os.Remove(f"{filename}.webp")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',nargs=1,required=True,help="name of the webp file")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    arg = parser.parse_args()
    convert(arg.filename)