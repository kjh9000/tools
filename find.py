#!/usr/bin/python3
# find.py
# Just a little script to make the find command easier to use.
# github.com/kjh9000

import os
query = input("Search term: ")
path = input("Directory to look in (/ is default): ")
if path == '':
    path = '/'
os.system("find " + path + " -iname *" + query + "*")
input('Done.')
