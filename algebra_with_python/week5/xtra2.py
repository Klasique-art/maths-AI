import matplotlib.pyplot as plt
import numpy as np

# the question in notebook. 1. find linear function. 2. find y intercept

# x is time and y is profit (in mil) 
x1 = 5
y1 = 10
x2 = 25
y2 = 4

# develop the equation
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1 # y intercept
print("y =", m, "x +", b)

# for the graph
xmin = 0
xmax = 50
ymin = 0
ymax = 16

# for the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# basic setup for the graph
fig, ax = plt.subplots()
ax.axis([xmin,xmax,ymin,ymax])
ax.plot([xmin,xmax], [0,0], 'b')
ax.plot([0,0], [ymin,ymax], 'b')
ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 1))

# add details to graph
ax.set_xlabel("Time")
ax.set_ylabel("Profit")
plt.grid(True)

# plot the linear functions
plt.plot([xmin,xmax], [y3,y4], 'r')

plt.show()