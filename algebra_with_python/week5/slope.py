import matplotlib.pyplot as plt

x1 = 1
y1 = 7
x2 = 2
y2 = 10

# developing equations
# slope is m
m = (y2 - y1) / (x2 -x1)
# y intercept is b
b = y1 - m*x1 # y = mx + b

# for the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# for the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# basic setup for graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax], [0,0], 'b') #blue x axis
plt.plot([0,0], [ymin,ymax], 'b') #blue y axis

# plot the linear functions as a red line
plt.plot([xmin,xmax], [y3,y4], 'r')
# the equation is
print("y =", m, "x +", b)

plt.show()