#!/bin/bash
# a small bash script to simultaenously rename multiple files in a dir
# i didnt author it just altered it a bit

# path to files renamed. this script should be ran in a didffferent dir than
# the files to be renamed or it will be renamed and wont be easy to find
cd / your path here

# currently its set up to rename up to 999 file with mp4 extension.
i=0
for file in *; do
    mv "$file" "$(printf %03d $i).mp4"
    i=$((i+1))
done
