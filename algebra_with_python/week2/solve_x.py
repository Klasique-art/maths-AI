# solving for x in python
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols("x")

# put equation here
eq = 2*x - 4 # 2x - 4 = 0

print("x =", solve(eq, x))