#!/usr/bin/python3
# sed.py - Find and replace text.
# Just a little script to make the sed command easier to use. It overwrites the
<<<<<<< HEAD
# original file, and saves a copy of the original with the same name and a .backup
# extension appended.
# kjh9000@github.com

import os, sys

# Gets the file name and checks if valid invalid. Also allows the ls option.
=======
# original file, and optionally saves a copy of the original with the same name
# and a .backup extension appended.
# kjh9000@github.com

import os

# Gets the file name and checks if valid invalid.
>>>>>>> cc17922a5e8e447b094ce1b5de80cb76c3c42538
filename = False

while os.path.isfile(filename) == False:
    filename = input('File: ')
    if os.path.isfile(filename) == False:
        print("Invalid file.")
<<<<<<< HEAD
term = input("Find: ")
replace = input("Replace: ")
=======

# Gets the find and replace text
term = input("Text to find: ")
replace = input("Text to replace it with: ")

backup=input("Create a back up of the original file? {Y/n) ")
>>>>>>> cc17922a5e8e447b094ce1b5de80cb76c3c42538

# The tempfile will be deleted. Be certain you don't have a file named 
# 123abcxyz54321 in the directory you're working in.
tempfile = "123abcxyz54321"

<<<<<<< HEAD
os.system("sed s/'" + term + "'/'" + replace + "'/g " + filename + " > " + tempfile)
os.system("cat " + filename + " > " + filename + ".backup")
os.system("cat " + tempfile + " > " + filename)
os.system("rm " + tempfile)
=======
# Performs the sed query
os.system("sed s/'" + term + "'/'" + replace + "'/g " + filename + " > " + tempfile)

# Creates a backup if the user desires it
if backup in ['n','N']:
    os.system("cat " + tempfile + " > " + filename)
    os.system("rm " + tempfile)
else:
    os.system("cat " + filename + " > " + filename + ".backup")
    os.system("cat " + tempfile + " > " + filename)
    os.system("rm " + tempfile)
>>>>>>> cc17922a5e8e447b094ce1b5de80cb76c3c42538
input("Done.")
