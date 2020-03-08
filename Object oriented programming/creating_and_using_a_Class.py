#Creating the dog class
class Dog(object):
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age atributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

#A function that is part of a class is a method
#init is sepcial method that runs automatically whenever a new instance of the class is made, must start with self
#any variable with a prefix of self is available to every method of the class

#Making an instance/ multiple instances:
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")	#accessing attributes 
print(f"My dog is {my_dog.age} years old.")

your_dog = Dog('Lucy', 3)

#Calling methods, use dot notation
my_dog.sit()
my_dog.roll_over()



