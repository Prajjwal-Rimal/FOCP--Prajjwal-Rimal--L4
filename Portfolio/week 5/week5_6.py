""" Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs"""

import sys

f = open(sys.argv[1], 'r')
f.seek(0)
stri = f.read()
print(stri)
f.close()

f = open(sys.argv[1] + "1" + ".txt", 'w')
f.write(stri)
f.close()
