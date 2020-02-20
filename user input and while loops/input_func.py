# input() function pauses your program and waits for a user to enter something
message = input("Teel me something. ") #add a space before closing quotes
print(message)

#prompt longer than one line:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}.")

# Using int():
age = input("How old are you? ") #whatever is entered will be returned as a string here

# to use response as a number i.e. for a comparison in an if statement, need to convert to int
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you are older.")


