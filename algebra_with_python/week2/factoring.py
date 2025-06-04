import sympy
from sympy import symbols

x, y = symbols("x y")

# equation set = 0, ready to solve
# eq = 2*x + 10*y + 4
eq = x**3 - 2*x**2 - 5*x + 6

print(sympy.factor(eq))