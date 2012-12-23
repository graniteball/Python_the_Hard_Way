# and and not
print "Using 'and' and 'not' and 'or'"
print "True and False should be equal to %s" % (True and False)
print "True or False should be equal to %s" % (True or False)
print "Not (True and False) should be equal to %s\n" % (not (True and False))

# del
print "Using 'del'"
mylist = ['John', 'Paul', 'George', 'Ringo']
print "%r" % mylist
del mylist[0]
print "Goodbye John %r" % mylist
del mylist[1:3]
print "Just Paul left %r" % mylist
mylist = ['John', 'Paul', 'George', 'Ringo']
del mylist[:]
print "Now it is empty %s\n" % mylist

# from
print "Using 'from'"
from sys import argv
script, arg1, arg2 = argv
print "The name of the script is %s" % script
print "The first arguement is %s" % arg1
print "The second arguement is %s\n" % arg2

# while
print "Using 'while'"
counter = 0
while (counter <= 10):
	print "Counter = %d" % counter
	counter += 1


# as and for and in
print "Using 'as' and 'for' and 'in'"
import random as rnd
for i in range(10):
	print "Random number = %d" % rnd.randint(1,10)
print ""
	
# if and elif and else
print "Using 'if' and 'elif' and 'else'"
my_number = int(raw_input("Input a number 1-10 > "))
if my_number <= 10:
	print "That is a small number"
elif my_number <=100:
	print "That is a medium number"
elif my_number > 100:
	print "That is a big number"
else:
	print "Something went wrong!"
print ""
	
# global
print "Using 'global'"
def my_function():
	global x
	x = 10
	y = 20

my_function()
# print "y should be undefined and is %r\n" % y
print "x should be defined and is %r\n" % x

# with
print "Using 'with'"
with open('ex15_sample.txt', 'r') as input_file:
	print "%s\n" % input_file.read()
	
# assert
print "Using 'assert'"
my_number = 2
print "This assert should pass\n"
assert my_number == 2
# print "This assert should fail\n"
# assert my_number == 3

# pass
print "Using 'pass'. Nothing should happen\n"
pass

# Generators and yield and return and def

print "Using generators and 'yield' and 'return' and 'def'"

# Build and return a list
def firstn(n):
	num, nums = 0, []
	while num < n:
		nums.append(num)
		num +=1
	return nums

def firstn_better(n):
	num = 0
	while num < n:
		yield num
		num +=1
		
highest_number = 1000000
sum_of_first_n = sum(firstn(highest_number))
print "Sum of first %d numbers is %d (not using yield)" % (highest_number, sum_of_first_n)
sum_of_first_n = sum(firstn_better(highest_number))
print "Sum of first %d numbers is %d (using yield)\n" % (highest_number, sum_of_first_n)

# break
print "Using 'break'"
print "Should list all numbers 0 to 9, but will break after 5"
for i in range(10):
	print i
	if i == 5:
		print ""
		break

# except and try
print "Using 'except' and 'try' to catch an exception"
try:
	bogus_filename = open("BogusFileName")
except:
	print "Open operation failed, so I am handling the error\n"
	
# class
print "Using 'class'"

class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print "I AM CLASSY APPLES!"
		
thing = MyStuff()
thing.apple()
print thing.tangerine
print ""
	
# exec
print "Using 'exec'"
exec ("for i in range(1,6): print i,")
print ""

# raise and finally
print "Using 'raise' and 'finally'"

################
#class YesNoException(Exception):
#   def __init__(self):
#      print 'Invalid value'


#answer = 'y'

#if (answer != 'yes' and answer != 'no'):
#   raise YesNoException
#else:
#   print 'Correct value'
##################


class MyException(Exception):
	def __init__(self):
		print "An exception was raised!"

#raise MyException
print "The exception was commented out"
print "This is the next line of code\n"

# finally:
# 	print "Print this line of code, even though the exception was raised"

# continue
print "Using 'continue' to make spaghetti code"
for i in range(10):
	print "This is the first print, before the continue"
	continue
	print "This is after the continue. It should never be seen."
print ""

# is
print "Using 'is'. Yes, 'is'."
print "None == None evaluates to %r" % (None == None)
print "None is None evaluates to %r" % (None is None)
print "True is True evaluates to %r" % (True is True)
print "[] == [] evaluates to %r" % ([] == [])
print "[] is [] evaluates to %r" % ([] is [])
print "'Python' is 'Python' evaluates to %r\n" % ("Python" is "Python")

# lambda
print "Using 'lambda'"
for i in range (1,6):
	a = lambda x: x*x
	print "i = %d, i squared = %d" % (i, a(i))
print ""




