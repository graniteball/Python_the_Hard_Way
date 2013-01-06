## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet
		self.pet = None

## Enployee is-a Person	
class Employee(Person):
	
	def __init__(self, name, salary):
		## Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
	
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a fish
class Salmon(Fish):
	pass
	
## Halibut is-a-fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")
print "The dog's name is %s" % rover.name

## satan is a Cat
satan = Cat("Satan")
print "The cat's name is %s" % satan.name

## mary is-a Person
mary = Person("Mary")
print "The person's name is %s" % mary.name

## frank is-a Employee
frank = Employee("Frank", 120000)
print "The employee's name is %s" % frank.name
print "The employee's salary is $%s" % frank.salary

## Frank has-a pet
frank.pet = rover
print "Frank's pet is %s" % frank.pet.name

# flipper is-a fish
flipper = Fish()

#crouse is-a salmon
crouse = Salmon()

#harry is-a halibut
harry = Halibut()


	