# Date: 19-06-24
# Write a program to solve a DC circuit using numpy
# In Numpy, a linear algorithm called 'linalg' is used to solve the DC circuit

import numpy as np
branch_equations = np.array([[8,-5,2], [10,-16,3], [2, 3, -5]]) # These are three loop equations
branch_voltages =  np.array([0, 0, -6])
branch_currents = np.linalg.solve(branch_equations,branch_voltages) # Solving the three equations to obtain the current of each loop
# here we formulate the given loop equations into the matrix form of: A = X*B
# And solve it as: X = A*B ^ -1 (A x B inverse)
print('Branch currents are: \n',branch_currents)
wheatStoneBridgeCondition = branch_currents[0] - branch_currents[1] # This value should be 0 for a balanced wheatStone Bridge.
print("Wheatstone Bridge current value: ",wheatStoneBridgeCondition)