import matplotlib.pyplot as plt
from sympy import symbols
from sympy.solvers import solve

# The number of people afflicted with the common cold in the winter months dropped steadily by 50 each year since 2004 until 2010. in 2004, 875 people were inflicted. Find the linear function that models the number of people afflicted with the common cold C as a function of the year t. When will no one be afflicted?

# we can say 2004 (time 0)

x1 = 0
y1 = 875
x2 = 1
y2 = 825 #if it drops by 50 then by year 1 (2004 is year 0), it'll be 825

# develop the equation
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print("y =", m, "x +", b)

# for the graph
xmin = 0
xmax = 18
ymin = 0
ymax = 900

# for the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# basic setup for the graph
fig, ax = plt.subplots()
ax.axis([xmin,xmax,ymin,ymax])
ax.plot([xmin,xmax], [0,0], 'b')
ax.plot([0,0], [ymin,ymax], 'b')

# add details to graph
ax.set_xlabel("Time")
ax.set_ylabel("People afflicted")
plt.grid(True)

# plot the linear functions
plt.plot([xmin,xmax], [y3,y4], 'r')

# in what time will the number of C cases be 0 (no one afflicted)?
x = symbols('x')

eq = 875 - 50*x

solution = solve(eq, x)
print(f"The time no one will be afflicted is {float(solution[0])}, ({2004 + int(solution[0])})")

plt.show()
