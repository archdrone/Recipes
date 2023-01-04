import os
import time
import sys


minutesLeft = 60
while minutesLeft > 0:
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} minutes remaining.".format(minutesLeft))
    sys.stdout.flush()
    time.sleep(600)
    minutesLeft -= 10

print("Times up!")
os.system("taskkill /im chrome.exe")
os.system("taskkill /im firefox.exe")

