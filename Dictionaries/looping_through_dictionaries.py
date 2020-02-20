user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi'
	}

#Looping through all Key-Value pairs using items() method:
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"\nValue: {value}")

# Looping through all Keys using keys() method

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
for name in favorite_languages.keys():  
	print(name.title())
# Looping through keys is default so same result would come from:
for name in favorite_languages:
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take  our poll.")

#looping through keys in a particular order
for name in sorted(favorite_languages.keys()):
	print(name.title())
print(favorite_languages)

#Looping through  all values
for language in favorite_languages.values():
	print(language.title())

# loop through values and omit repeats using set():
for language in set(favorite_languages.values()):
	print(language.title())

#Note on sets: are made using {} just like a dictionary:
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
