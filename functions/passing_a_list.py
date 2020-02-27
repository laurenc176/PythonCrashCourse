def greet_users(names):
	"""Print a simple greeting to each user in the list"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modifying a list in a function
unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design until none are left."""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a function from modifying a list
#you can pass a function a copy of the list by using slice notation:
#function_name(list_name[:]) 
print_models(unprinted_designs[:], completed_models)