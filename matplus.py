#!/usr/bin/python3
import os

# this script scrubs metaddata using metadata analysis tool (MAT)
# must have mat2

# this line sets the default directory of the files to be scrubbed
# if youre going to run this script in the same directory as the files
# to be scrubbed, you comment the line below out. 
os.system("cd /path to files")

filename = os.getcwd() + "/" + input("Name of file to scrub: ")
os.system("mat2 --inplace " + filename)
print("Done.")
os.system("mat2 -s " + filename)
input()
