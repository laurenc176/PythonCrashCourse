# input() function pauses your program and waits for a user to enter something

#print(message)

#prompt longer than one line:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}.")