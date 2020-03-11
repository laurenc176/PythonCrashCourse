import matplotlib.pyplot as plt 

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14) #styles the tick marks
#plt.show()

# -------------------------------------------------------------------------------
#Calculating data Automatically

x_vals = range(1,1001)
y_vals = [x**2 for x in x_vals] #list comp generates the squares 

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.scatter(x_vals,y_vals, s=10)

#can change colors with the name of the color in quotes, using RGB, or colormap
#Examples:
#ax.scatter(x_vals, y_vals, c='red', s=10)
#ax.scatter(x_val,y_vals, c=(0, 0.8, 0), s=10)	# this would be light green dots

# c specifies to assign color to each point based on y_value and cmap specifies the color map:
# more info at https://matplotlib.org/ go to examples, scroll down to color, click colormap reference
#ax.scatter(x_vals,y_vals, c=y_vals, cmap=plt.cm.Blues, s=10)   

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000]) # axis() method requires 4 values: xmin, xmax, ymin, ymax

plt.show()