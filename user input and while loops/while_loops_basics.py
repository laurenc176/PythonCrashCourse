current_num = 1
while current_num <= 5:
	print(current_num)
	current_num += 1

prompt = "Tell me something and I'll repeat it back to you"
prompt+= "\nEnter 'quit' to end the program"

message = "" #keeps track of whatever user enters
while message != 'quit':
	message = input(prompt)
	print(message)			#this will print 'quit' when the user enters quit

while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':	#adding this if statement will prevent 'quit' from being printed
		print(message)

# Using Flags
# example: in a game when several diff events can end the game

prompt = "Tell me something and I'll repeat it back to you"
prompt+= "\nEnter 'quit' to end the program"

active = True  #program will start in active state, as long as its true loop will continue to run
while active:
	message= input(prompt)

	if message == 'quit': 
		active = False	#will stop the loop
	else:
		print(message)

#although above was kept simple, using flag makes it easier to ass more tests (ie. elif statements)

# Using break to exit a loop

p = "\nPlease enter the name of a city you have visited:"
p+="\n(Enter 'quit' when you are finished.)"

while True:			#will run forever unless it reaches a break statement
	city = input(p)

	if city == 'quit':
		break
	else:
		print(f"I'd love to visit {city.title()}.")	

# Using continue in a loop
current_number = 0
while current_number < 10:
	current_number +=1
	if current_number % 2 == 0:
		continue					#if number is even it won't be printed

	print(current_number)	


