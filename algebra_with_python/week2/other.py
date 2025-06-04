from sympy import *

var("x y")

# first equation set equal to zero, ready to solve
first = 2*x + 10 - y

# sympy syntax for equation equal to zero, ready to factor
eq1 = Eq(first,  0)

# sympy solve for x
sol = solve(eq1, x)

# show factored results
print("x =", sol[0])