tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

for name in ['Sue', 'Alan', 'BJ', 'Alison']:
	print "\fMy name is %s." %name
	print "This is my address"
	print "\x33 Festival Court"
	print "Newark\x2C Deleware."