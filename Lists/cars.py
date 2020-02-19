#organizing a list

#sorting a list permanently with the sort() method, can never revert 
#to original order
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#can also do reverse
cars.sort(reverse=True)
print(cars)

# sorted() function sorts  a list temporarily **also will accept a
#reverse=True argument
cars = ['bmw','audi','toyota','subaru']
print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

