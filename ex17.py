from sys import argv #import argv function to get arguements
from os.path import exists #import exists function to check if files exist

script, from_file, to_file = argv #get my command line inputs

print "Copying from %s to %s" % (from_file, to_file) #Show the user the names if the input and output files

# we could do these two on one line too, how?
# in_file = open(from_file) #get a file handle on out input file
# indata = in_file.read() #read the contents of the input file
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata) #print the length of the input file contents in characters

print "Does the output file exist? %r." % exists(to_file) #check if the output file exists
print "Ready, hit RETURN to continue, CTRL-C to abort." #give the user a chance to bail or continue
raw_input()

out_file = open(to_file, 'w') #get a handle to the output file
out_file.write(indata) #write the contents of the input file to the output file

print "Alright, all done." #duh

out_file.close() #clean up
# in_file.close()
