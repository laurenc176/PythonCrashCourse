#Numerical Lists

#using the range() function range([start],[stop(*up to but not including)],[increment(*not requried but can include)])
# Examples:
for value in range(5):
	print(value)
print('\n')
for value in range(1,5):
	print(value)
print('\n')
for value in range(1,10, 2):
	print(value)
print('\n')

#Using range to make a list
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# can also do (more efficient):
squares = []
for val in range(1,11):
	squares.append(val**2)
print(squares)

#simple Statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # min of list
print(max(digits)) # max of list
print(sum(digits)) # sum of list

#List comprehensions
# allows you to generate a list in one line of code
squares = [value**2 for value in range(1,11)]
print(squares)
#begin with descriptive name of list (squares), next open brakets and define the expression for the values you want to 
#store in the new list (value**2), then write a for loop to generate the numbers to feed into the expression, then close the brakets
