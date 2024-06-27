# Write a python program to optimise the power distribution for maximum profit.
# Use linear optimization in scipy for the same

from scipy.optimize import linprog
c = [4,7]
A = [[1,1]]
b = [10]
x0_bounds = (2,10)
x1_bounds = (5, 9)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
print(res.fun)
print(res.x)