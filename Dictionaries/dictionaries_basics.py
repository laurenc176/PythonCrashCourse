#Simple dictionary
# key : value  pair
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#adding to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#As of Python 3.7, dictionaries retain the order in which they were defined
#when you print or loop through elements, you will see them in the same order in which they were added

#modifying values
alien_0['color'] = 'yellow' #changes color from grren to yellow

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' :' medium'}
print(f"Original position: {alien_0['x_position']}")

#move alien to the right
#Determine how far to move alien based on current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:	
	#This must be a fast alien
	x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#removing key value pairs
alien_0 = {'color': 'green', 'points':5}
del alien_0['points'] #deleted key value pair is removed permanently
print(alien_0)

#Using get() to access values
alien_0 = {'color': 'green', 'speed':'slow'}
point_value = alien_0.get('points', 'No point value assigned.') #if key is not there, will print second argument
# If you don't add the second argument Python will return None
print(point_value)
