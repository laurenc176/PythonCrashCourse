import matplotlib.pyplot as plt 

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

x_range = range(1,5000)
y_vals = [x**3 for x in x_range]

fig,ax = plt.subplots()
#ax.scatter(x_values, y_values)
ax.scatter(x_range, y_vals, c=y_vals, cmap=plt.cm.Reds)

plt.show()