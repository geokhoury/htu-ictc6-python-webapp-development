# Car Capacity

# declare variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# declare other variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = int(cars_driven * space_in_a_car)
average_passengers_per_car = int(passengers / cars_driven)

# > print some values

# print("There are", cars, "cars available.")
print(f"There are cars {cars} available.")

# print("There are only", drivers, "drivers available.")
print("There are only %d drivers available" % drivers)

# print("There will be", cars_not_driven, "empty cars today.")
empty_cars_msg = "There will be {msg} empty cars today."
print(empty_cars_msg.format(msg=cars_not_driven))

# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car, "in each car.")
