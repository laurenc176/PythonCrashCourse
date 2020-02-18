#TUPLES = IMMUTABLE "LISTS"
#use when you want to store a set of values that should not be changed throughout the life of a program

#made by using ( , )
dimensions = (200,50)
#indexed the same as lists
print(dimensions[0])
print(dimensions[1])

#looping through a tuple
for d in dimensions:
	print(d) 

#although you cannot modify a tuple - i.e. dimensions[0] = 250 (will throw an error)
# you can assign a new value to a variable that represents a tuple, redefine it:
dimensions = (200, 50)
print("original dimensions: ", dimensions)

dimensions = (400, 100)
print('\nModified dimensions: ', dimensions)
