def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "Multipying %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the ectra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That beomes: ", what, "Can you do it by hand?"

print"Yes, the answer is -4391"