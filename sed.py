#!/usr/bin/python3
# sed.py - Find and replace text.
# Just a little script to make the sed command easier to use. It overwrites the
# original file, and saves a copy of the original with the same name and a .backup
# extension appended.
# kjh9000@github.com

import os, sys

# Gets the file name and checks if valid invalid. Also allows the ls option.
filename = False

while os.path.isfile(filename) == False:
    filename = input('File: ')
    if os.path.isfile(filename) == False:
        print("Invalid file.")
term = input("Find: ")
replace = input("Replace: ")

# The tempfile will be deleted. Be certain you don't have a file named 
# 123abcxyz54321 in the directory you're working in.
tempfile = "123abcxyz54321"

os.system("sed s/'" + term + "'/'" + replace + "'/g " + filename + " > " + tempfile)
os.system("cat " + filename + " > " + filename + ".backup")
os.system("cat " + tempfile + " > " + filename)
os.system("rm " + tempfile)
input("Done.")
