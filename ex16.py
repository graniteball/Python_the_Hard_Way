from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "Truncating the file.  Goodbye!"
# target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

newline = "\n"

target.write(("%s%s%s%s%s%s") % (line1,newline,line2,newline,line3,newline))

# target.write(line1 + newline + line2 + newline + line3 + newline)

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()

print "But wait, there's more!"
print "Now we will read the file and print it"

target = open(filename)
print target.read()

print "And finally, really finally, we close it."
target.close()
