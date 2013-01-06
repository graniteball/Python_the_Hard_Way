def function1():
	print "you chose 1"
def function2():
	print "you chose 2"
def function3():
	print "you chose 3"
	
#
# switch is our dictionary of functions
switch = {
	'one':function1,
	'two':function2,
	'three':function3
	}
#
#chice can either be 'one', 'two', or 'three
choice = raw_input('Enter one, two, or three: ')
#call one of the functions
try:
	result = switch[choice]
except KeyError:
	print 'I didn\'t understand your choice.'
else:
	result()