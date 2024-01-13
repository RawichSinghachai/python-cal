import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x,a = sym.symbols('x a')
y =x**4 - 8*x**3 +12*x -5

ans = sym.simplify(sym.diff(y,x))

sol = ans.subs(x,-2)
print(sol)