#!/usr/bin/python3

# datausecalc.py -  A data usage calculator for Tello users
# github.com/kjh9000

''' Instructions - Copy and paste the wall of text rom the website and paste it into
datausecalc.txt. Note the potential for fencepost errors. You are responsible for 
choosing what days to include in the calculation.

'''

import re

try:
    testtext = open('datausecalc.txt')
except (NameError, FileNotFoundError):
    print("This program requires a datausecalc.txt file. You can either create it or download it.")
else:
    sum = 0
    count = 0
    for i in re.compile(r'(\d{1,5}\.\d{1,2}|\d{1,5}) MB').findall(testtext.read()):
        count += 1
        sum += float(i)
    if sum == 0:
        print("datausecalc.txt contains no useful data.")
    else:
        print("You have used about", round(sum, 2), "MB of data in", count, "days.")
        print("You use an average of " + str(round(sum / count, 2)) + " MB per day.")
