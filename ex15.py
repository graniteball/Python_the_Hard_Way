# get the library that lets you pass in arguements
from sys import argv

# get the name of the script and the name of the file passed in
script, filename = argv

# get a file handle on the file name passed in
txt = open(filename)

# print the filename, then the file handle, then the contents of the file
print "Here's your file %r:" % filename
print "Here's the file handle %r:" % txt
print txt.read()
txt.close()

# now get the file name from the user
file_again = raw_input ("Type the filename again> ")

#repeat the process above with the user-input file name
txt_again = open(file_again)

print "Here's the file handle %r:" %txt
print txt_again.read()
txt_again.close()
