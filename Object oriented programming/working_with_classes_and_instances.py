#Modifying the attributes of an instance
#Can modify the attributes directly of write methods that update attributes in specific ways

#The Car Class

class Car(object):
	"""A simple attempt to represent a car."""
	def __init__(self, make model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


#Setting a default value for an attribute
#Attributes can be defined without being passed as parameters in the __init__() method
class Car(object):
	"""A simple attempt to represent a car."""
	def __init__(self, make model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car.read_odometer()

#Modifying attribute values: 3 ways
#One: change the value directly through and instance
my_new_car.odometer_reading = 23

#Two: set the value through a method

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		self.odometer_reading = mileage
my_new_car.update_odometer(23)

#extend update_odometer method to amke sure it can't be rolled back:
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")


#Three: increment the value through a method.
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
		

