# while loops are better than for loops to use when you want to modify dicts and lists
#easier to keep track of things

# Start with users that need to be verified, 
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users: #will run  as long as list is not empty
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish','cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

#Filling a dict with user input
responses = {} #start with empty dict
#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb today? ")

	#Store the response in a dict
	responses[name] = response

	# Find out if anyone else is taking the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

#Polling is complete. Show results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")