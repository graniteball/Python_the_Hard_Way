from sys import argv
import collections

script, input_file = argv

states_file = open(input_file)
capitals = {} # set up the capitals dictionary
line = states_file.readline() # get the first line (header) and initialize line so it is not ""
line = states_file.readline() # get the first one
while line != "":
	split_line = line.split(',')
	capitals[split_line[0]] = split_line[2] 
	line = states_file.readline() # get the next one

# Now print an alphabetized list of state capitals

print capitals
print capitals.items()
# ordered_capitals = collections.OrderedDict(sorted(capitals.items(), key=lambda t: t[0]))
ordered_capitals = collections.OrderedDict(sorted(capitals.items(), key=lambda t: t[0]))

for state in ordered_capitals:
	print "The capital of %s is %s" % (state, capitals[state])
