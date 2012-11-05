cars = 100 # Total cars in fleet
space_in_a_car = 4.0 # Seats per car
drivers = 30 # Number of afailable drivers
passengers = 90 # Number of passengers that we need to carry
cars_not_driven = cars - drivers # Number of cars that will sit idle
cars_driven = drivers # Number of cars that will be driven
carpool_capacity = cars_driven * space_in_a_car # Total number of people in carpool
average_passengers_per_car = passengers / cars_driven # Average passengers per car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
