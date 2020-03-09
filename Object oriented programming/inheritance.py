#When writing a new class based on an existing class, often will want to call the __init__()
#method from the parent class.  Will initialize any attributes that were defined in the 
#parent __init__() method and make them available to the child class

#Example: electric Car

#Car class is the parent class:
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

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles

#Definiing attributes and methods for the child class
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electic vehicles"""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year) #super() -special function, allows you to call method from parent
		self.battery_size = 75 #will only be associated with electric, not parent

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a  {self.battery_size}-kWh battery.")

#Overriding methods from the parent class: define a method in child with
#same name as method you want to override in parent
#Example: say Car has a fill gas tank method:	
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print(f"This car doesn't need a gas tank.")



#Instances as attributes, example: might notices you are adding many attributes
#and methods specific to the car battery. Can stop and move those to a class called Battery
class Battery(object):	#doesn't inherit from any other class
	"""A simple attempt to modle a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a  {self.battery_size}-kWh battery.")


#Changes to electric car class now that battery was made:
class ElectricCar(Car):
	"""Represents aspects of a car, specific to electic vehicles"""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year) 
		self.battery = Battery() 

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about  {range} miles on a full charge")
		

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()


	