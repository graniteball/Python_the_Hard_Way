def list_builder(len, inc):
	i = 0
	numbers = []

#	while i < len*inc:
	for i in range(0, len*inc, inc):
#		print "at the top i is %d" % i
		numbers.append(i)

#		i += inc
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i
	return(numbers)
	
numbers = list_builder(int(raw_input("Enter list length > ")), int(raw_input("Enter list increment > ")))

print "The numbers: "

for num in numbers:
	print num