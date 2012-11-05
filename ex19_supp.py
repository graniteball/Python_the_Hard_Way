def math_test(x,y):
		x = float(x)
		y = float(y)
		print "X = %5.3f, Y = %5.3f" % (x, y)
		print "X + Y = %5.3f" % (x + y)
		print "X - Y = %5.3f" % (x - y)
		print "X * Y = %5.3f" % (x * y)
		print "X / Y = %5.3f" % (x / y)

print "\nHard coded integers"
math_test(1, 2)
print "\nHard coded floats"
math_test(1.0,2.0)
print "\nGet integers from user"
math_test(raw_input("Input X > "),raw_input("Input Y > "))
print "\nDo some math in the input parameters"
math_test(0.5+0.5, 1+1)
print "\nSet variables ahead of time"
i = 5
j = 8
math_test(i,j)