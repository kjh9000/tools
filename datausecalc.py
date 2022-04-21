#!/usr/bin/python3

# datausecalc.py -  A data usage calculator for Tello users
# github.com/kjh9000

''' Instructions - Copy and paste the wall of text from the website and paste it 
into datausecalc.txt. Note the potential for fencepost errors. You are responsible
for choosing what days to include in the calculation.
'''

import re

try:
	testtext = open('datausecalc.txt').read()

except (NameError, FileNotFoundError):
	print("This program requires a datausecalc.txt file. You can either create it or download it.")

else:

	# create a list of MBs of data used, iterate through the list and store in total
	data = re.findall('\d{1,5}\.\d{1,2}|\d{1,5} MB',testtext)
	total = 0
	for i in data:
		total += float(i)

	# counter counts the number of days
	counter = testtext.count('MB')
	
	if total == 0:
		print("datausecalc.txt contains no useful data, or you used no data.")
	else:
		print("You have used about", round(total, 2), "MB of data in", counter, "days.")
		print("You use an average of " + str(round(total / counter, 2)) + " MB per day.")

