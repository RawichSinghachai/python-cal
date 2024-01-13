import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
import time

t = time.time()


x,a = sym.symbols('x a')
y =2*x**3 + 7*x**2 -3*x +5

ans = sym.simplify(sym.diff(y,x,2))

sol = ans.subs(x,-2)
print(ans)

ela = time.time()-t
print(ela)