import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x,a = sym.symbols('x a')
ans = sym.limit((x**2-25)/(x-5),x,5)
print(ans)