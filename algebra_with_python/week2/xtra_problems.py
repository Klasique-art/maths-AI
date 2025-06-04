import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols("x")

# equation here
# eq = 2*x**2 + 1 # 2x + 1 = 0

# print(solve(eq, x))

# prompt users for equation
eq = input("Enter equation: 0 = ")

print("x =", solve(eq, x))