#	working with part of a list

#slicing a list
players = ['charles','martina', 'michael', 'florence', 'eli']
print(players[0:3]) #[start index: up to but not including index]
#If you omit 1st index, it will automatically start at 1st index
# if you omit last index, will automatically end at last index
print(players[:3])
print(players[2:])
# to do last 3 players, can use negative indexing:
print(players[-3:])

#Looping through a slice:
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]  #by omiting indexes this will make a copy of a list and we will have 2 different lists

my_foods.append('cannoli')
friends_foods.append('ice cream')

print(my_foods)
print(friends_foods)

#this doesn't work:
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream') #will append both items to both lists

print(my_foods)
print(friends_foods)



