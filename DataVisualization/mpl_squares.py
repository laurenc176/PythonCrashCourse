import matplotlib.pyplot as plt 

input_values = [1.0, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() # subplots() function can generate one or more plots on the same figure
# variable fig represents the entire figure or collection of plots that are generated
# variable ax represents a single plot in the figure

# Customizations:

ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14) #styles the tick marks

plt.show()

# Side note: to save plots automatically replace plt.show() with plt.savfig():
# plt.savefig('squares_plot.png', bbox_inches='tight')  # second arg here trims extra whitespace from the plot
# if you want the extra whitespace just omit the arg

