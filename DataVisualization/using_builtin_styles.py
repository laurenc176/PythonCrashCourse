# to see styles available on system go to terminal session and put in:
# >>> import matplotlib.pyplot as plt
# >>>plt.style.available

import matplotlib.pyplot as plt 

input_values = [1.0, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14) #styles the tick marks

plt.show()