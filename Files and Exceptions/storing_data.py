#json module allows you to dump simple Python data structures into a file and load
#the data from that file the next time the program runs. Can also be used to share data
#between different Python programs
#'Even better':Not specific to Python, so you can share data you store in JSON format with ppl who work
#in many other programming languages.  Useful, portable, easy to learn

#Using the json.dump() and json.load(), simple way to share data between two programs
#JSON(JavaScript Object Notation)

#json.dump() takes two arguments: a piece of data to store and a file object it can use to store the data
import json  #first import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'  #choose a filename to store list of numbers
with open(filename, 'w') as f:  #open in write mode
	json.dump(numbers, f)  #use json.dump() to store the list in the filename
--------------------------------------------------
#json.load()
import json

filename = 'numbers.json'
with open(filename) as f:
	numbers	= json.load(f)
print(numbers)

---------------------------------------------------
#Saving and Reading User-Generated Data, useful to use json
#because if you don't store your user's info somehow, you'll lose it when the program stops running
import json

#Load the username, if it has been stored previousl.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")

----------------------------------------------------
#Refactoring: process of breaking up previously written code into a series of functions with
#functions that have specific jobs.  Makes code cleaner, easier to understand, and easier to extend.

#Refactor remember me from above:
import json
def greet_user():
	"""Greet user by name"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")
	else:
		print(f"Welcome back, {username}!")

---------------------------------------------------------------
#Refactor greet_user()
import jason

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def greet_user():
	"""Greet the user by name"""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open (filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}.")

----------------------------------------------------------
#Refactor again:

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open (filename, 'w') as f:
		json.dump(username, f)
	return username


def greet_user():
	"""Greet the user by name"""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}.")






