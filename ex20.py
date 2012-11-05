from sys import argv

script, input_file = argv

def print_all(file_handle):
	# print the entire contents of the file
#	print "The current file handle is %r\n" % file_handle
	print file_handle.read()
	
def rewind(file_handle):
	# go back to the beginning of the file
#	print "The current file handle is %r\n" % file_handle
	file_handle.seek(0)
	
def print_a_line(line_count, file_handle):
	# read and print the current line the file handle is pointing to
#	print "The current file handle is %r\n" % file_handle
	print line_count, file_handle.readline(),

# open a file for reading	
current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now, let's rewind, kind of like a tape."

rewind(current_file)

print "\nLet's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)