x = "There are %d types of people." % 10 # creates a string in 'x' stubsituting 10 for the variable.
binary = "binary" # creates a string called 'binary' which is set to "binary"
do_not = "don't" # similar to above
y = "Those who know %s and those who %s." % (binary, do_not) #creates a string in 'y' substituting the values for the above two strings into the 'y' string

print x # duh
print y # duh

print "I said: %r." % x # print the literal value of x
print "I also said: '%s'. " % y # print the string y in single quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # create a string with a bariable in it

print joke_evaluation % hilarious # now fill in the variable

w = "This is the left side of..." # half of string
e = "a string with a right side." # other half of string

print w + e # concatinate the two substrings