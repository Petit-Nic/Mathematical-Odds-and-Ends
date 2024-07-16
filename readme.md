# Python code for mathematical odds and ends

## Purpose

This github repo contains python code I've developed since roughly 2020, related to my mathematical teaching and overall curiosity. Some of these might get upgraded to the repo with the code relevant to my research in due time

## File descriptions

Here is a description of the files currently in the repo. See each file for more details and comments:

* freeGroupWords.py: This file contains an algorithm to recursively build words in the free group on n generators and save the results in an appropriately named file. To get all words of length k run the file k+1 times

* carpets.py: This file contains an algorithm to color carpets with p colors, inspired by a talk by Colin Adams and his students at the Unknot V conference.

* plantSpirals.py: built when teaching a "Math for the Liberal arts class" (as with all the following files), this python code generates a picture of a plant whose petals are a certain distance away from each other. Make sure your python version has tkinter installed.

* sierpinski.py (and related sierp*.py): these files will build sierpinski triangles/squares at a given depth (to be changed in the code) and output the pictures as png files. The "*Arbitrary" files let you also determine how to split the triangle/rectangle and which parts to keep/toss. They require the graphics package provided as "graphics.py-5.0.1.post1.tar.gz", which is a wrapper for tkinter.

## License

I retain full copyright of the code, but I'm happy to let people use it upon request. Shoot me an email at petitnicola@gmail.com if you'd like to use any part of the repo (even just a code snippet).