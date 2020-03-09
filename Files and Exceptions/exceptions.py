#Handling exceptions

#ZeroDivisionError Exception, use try-except blocks
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

#This will crash if second number is 0
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	answer = int(first_number) / int(second_number)

#Prevent crash:
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)


#FileNotFoundError Exception
try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist")

#Analyzing Text
#Many classic lit are available as simple text files because they are in public domain
#Texts in this section come from Project Gutenberg(http://gutenberg.org/)
title = "Alice in Wonderland"
title.split()
filename = 'alice.txt'
try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist")
else:
	#Count the approx number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")

#Working with Multiple files, create a function
def count_words(filename):
	"""Count the approx number of words in the file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
				

#Fail silently - you don't need to report every exception
#write a block as usual, but tell Python to do nothing in the except block:
def count_words(filename):
	"""Count the approx number of words in the file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass #will fail silently, acts as a placeholder
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")