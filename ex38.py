ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')

more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) < 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print "Here is the stuff list %r" % stuff
print "Second element = %r" % stuff[1]
print "Loop back to the end of stuff %r" % stuff[-1] # woah! fancy
print "Here is the (removed) last element of stuff %r" % stuff.pop()
print "Here is the stuff list %r" % stuff
print "Here are all of the elements joined together separated by a space %r"% ' '.join(stuff) # what? cool!
# print "Here are all of the elements joined together separated by a space %r"% stuff.join(' ') # what? cool!
print "Join elements 3 to 5 (5 noninclusive) by '#' %r" % '#'.join(stuff[3:5]) # super stellar!

