from sys import argv
import pprint

script, input_file = argv

states_file = open(input_file)
capitals = {} # set up the capitals dictionary
states = [] #set up states list
line = states_file.readline() # get the first line (header) and initialize line so it is not ""
line = states_file.readline() # get the first one
while line != "":
	split_line = line.split(',')
	states.append(split_line[0])
	capitals[split_line[0]] = split_line[2] 
	line = states_file.readline() # get the next one

states.sort() # The list should have already been sorted from the file, but just in case...

# Now print an alphabetized list of state capitals

for state in states:
	print "The capital of %s is %s" % (state, capitals[state])

