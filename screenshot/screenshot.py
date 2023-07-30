import os
import argparse
import pyautogui
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="absolute path to the dir where the screenshots are saved", default=r"./images")
parser.add_argument("-s", "--seconds", help="the time (in seconds) between each screenshot", default=1)
parser.add_argument("-n", "--number", help="the number of screenshots to take", default=1)
args = parser.parse_args()
sec = args.seconds
if sec < 1:
    sec = 1
if os.path.isdir(args.directory[0]) != True:
    os.mkdir(args.path)
try:
    counter = 0
    while (counter < args.seconds):
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        file = current_time + ".jpg"
        image = pyautogui.screenshot(os.path.join(args.directory, file))
        print(f"{file} saved\n")
        time.sleep(sec)
        counter += 1
except KeyboardInterrupt:
    print("end of script by user intrerrupt")
