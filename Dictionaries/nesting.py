# Nesting - storing multiple dicts in a list, or a list of items as a value in a dict

#List of Dictionaries
aliens = []
# Make 10 green aliens.
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# List in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

# dictionary in a Dictionary:
users ={
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris'
		},
	} # has two keys aeinstein and mcure and value is a dict with each users info
for username, user_info in users.items(): #loop through users
	print(f"\nUsername: {username}") #once inside main loop, print username
	full_name = f"{user_info['first']} {user_info['last']}" #here is where we access inner dict
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}") #use each key to format and print info
	print(f"\tLocation: {location.title()}")

