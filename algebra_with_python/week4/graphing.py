import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
# dimensions
plt.axis([xmin,xmax,ymin,ymax]) #window size
# display axis lines
plt.plot([xmin,xmax], [0,0], "b") #blue x axis
plt.plot([0,0], [ymin,ymax], "b") #blue y axis

# plot a point
print("x \t y")
for x in range(xmin, xmax+1):
    y = 0.5*x + 1
    plt.plot([x], [y], "ro")
    print(x, "\t", y)

plt.show()