import matplotlib.pyplot as plt

# A town's population increases at a constant rate. in 2010 the population was 55,000. by 2012 the population had increased to 76,000 If this trend continues, predict the population by 2016.

# we can start from 2010 as time 0 (time on the x axis) 2012 is 2 years apart so we can increase by 2 years. we label 55,000 as 55 and 76k as 76.

x1 = 0 #time 0 (2010)
y1 = 55
x2 = 2 # 2 years apart
y2 = 76

# develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1) # slope
b = y1 - m*x1 # y intercept
print("y =", m, "x +", b)

# for the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 150

# for the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax], [0,0], 'b')
plt.plot([0,0], [ymin,ymax], 'b')

# add details to graph
ax.set_xlabel("time")
ax.set_ylabel("population")
plt.title("Population growth")
plt.grid(True)

# plot the linear functions
plt.plot([xmin,xmax], [y3,y4], 'r')

plt.show()