bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati' #replaces honda
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)
#inserting into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') #first is say where you want to place it, second is what you are putting in, doesn't replace
print(motorcycles)

#removing items

del motorcycles[0] #deletes first element
print(motorcycles)

#pop()method removes the last item in a list but can also be used after
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#can also remove using pop by stating the index
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#how to decide between pop() and del: if you don't want to use again, use del, otherwise use pop()

#remove item by value if you don't know its index, use remove(): **will only remove the first occurence of what is specified
motorcycles = ['honda','yamaha','suzuki']
motorcycles.remove('honda')

