import matplotlib.pyplot as plt 

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) # pass a sing(x,y),  s sets the size of the dot

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14) #styles the tick marks **not sure what 'which'means just yet 3/11/20

plt.show()