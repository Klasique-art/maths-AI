import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax], [0,0], "b")
plt.plot([0,0], [ymin,ymax], "b")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 2))

y = 2*x + 1
plt.plot(x,y,"r")

plt.show()