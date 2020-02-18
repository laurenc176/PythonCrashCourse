#organizing a list

#sorting a list permanently with the sort() method, can never revert 
# to original order (unless a copy is made first)
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#can also do reverse
cars.sort(reverse=True)
print(cars)

# sorted() function sorts  a list temporarily
cars = ['bmw','audi','toyota','subaru']
print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Can print a list in reverse order using reverse() method, changes it permanently 
# doesnt sort backward alphabetically, simply reverses order of the list
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

#other methods I already know:
len(cars)
cars[-1] # using -1 as an index will always return the last item in a list unless list is empty, then will get an error

