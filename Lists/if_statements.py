cars = ['audi','bmw', 'subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#ignoring case when checking equality:
car = 'Audi'
car == 'audi' #False

car.lower() == 'audi' #True, does't change original variable assignment ot lowercase

#Checking for inequailty
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")

#numerical comparisons
answer = 17

if answer != 42:
	print("That is not the correct answer, try again")

#multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  #False

age_0 >= 21 or age_1 >= 21 #True

#checking if value in a list
requested_topping = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_topping	#True
'pepperoni' in requested_topping 	#False

#Checking if a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

#Simple if statements:
# if conditional test:
	#do something

#once a condition is met, Python will exit the loop
#If Else statements
# if conditional test:
	# do something
# else:
	# do something else

#If, elif, else: same as above, can have as many elif statements as you want
#else always comes last but can be omitted:

age =12

if age < 4:
	price = 0
elif age < 18:
	price=25
elif age< 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}")

#sometimes omitting else will make code clearer
#in the below case it lets you know anyone 65 and older has a price of 20
age =12

if age < 4:
	price = 0
elif age < 18:
	price=25
elif age< 65:
	price = 40
elif age >= 65:
	price = 20
print(f"Your admission cost is ${price}")

#Testing multiple conditions
# better to use series of if statements because once a condition is met, Python will exit the loop
# below code would not work properly with if-elif-else block 
requested_topping = ['mushrooms','extra cheese']

if 'mushrooms' in requested_topping:
	print("Adding mushrooms")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese")

print("\nFinished making your pizza!")		
