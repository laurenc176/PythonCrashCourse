#For when you won't know ahead of time how many args a function needs to accept

#building a pizza, responds appropriately whether it receives 1 or 3 or 4 values
# '*' indicates arbitrary argument aka
def make_pizza(*toppings):   #*args (if looking through documentation)
	"""Summarize the pizza we are about to make"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

#Mixing positional and arbitrary arguments
#***The Parameter that accepts the arbitrary arg must be placed last

def make_pizza2(size, *toppings):
	"""Summarize the pizza we are about to make"""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

#Using Arbitrary Keyword Arguments
#Sometimes: Arbitrary num of args BUT won't know ahead of time what info will be passed to the function
#Example: buliding user profiles

def build_profile(first, last, **user_info):  # aka **kwargs 
	"""Build a dictionary containing everything we know about a user."""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)