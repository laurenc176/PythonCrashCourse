#Defining a function
def greet_user(username): 		# define the function, the variable username is the parameter
	"""Display a simple greeting."""	# Include doctstring describing what it does
	print(f"Hello, {username.title()}")		
greet_user('lauren')  #call the function , 'lauren' is an example of an argument

#Postional arguments: order matters
def describe_pet(animal_type, pet_name):
	"""Display info about pet."""
	print(f"\nI have an {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'willie') # works
describe_pet('harry', 'hampster') # doesn't work

# Keyword arguments, order doesn't matter but need to use exact names
describe_pet(pet_name='harry', animal_type='hamptser')	# works

#Defined arguments
def describe_pet(pet_name,animal_type='dog'):		#will default to dog unless you specify kwarg and change it
	"""Display info about pet."""
	print(f"\nI have an {animal_type}")
	print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# Making an agrument optional
def get_formatted_name(first_name, last_name, middle = ''): #will default to no middle name unless added
	if middle:
		full_name = f"{first_name} {middle} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name

# Returning a dictionary
def build_person(first_name, last_name, age=None):
	""" Return a dictionary of info about a person"""
	person = {'first':first_name, 'last': last_name}
	if age:
		person['age']= age
	return person

# using a function with a while loop:
def get_formatted_name(first_name, last_name): 
	full_name = f"{first_name} {last_name}"
	return full_name.title()

	while True:
		print("\nPlease tell me your name: ")
		f_name = input("first name: ")
		l_name = input("Last name: ")

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}")

# with a conditional:
def get_formatted_name(first_name, last_name): 
	full_name = f"{first_name} {last_name}"
	return full_name.title()

	while True:
		print("\nPlease tell me your name: ")
		print("(enter 'q' at any time to quit")

		f_name = input("first name: ")
		if f_name == 'q':
			break
		l_name = input("Last name: ")
		if l_name == 'q':
			break
	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}")

