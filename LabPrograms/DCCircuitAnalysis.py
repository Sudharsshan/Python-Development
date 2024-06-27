# Date: 27-06-24
# A python program to analyse the current flowing through the branches of the circuit
'''
  (+)   (-)
 ---24V---4ohm---------
 |                    |
 |---1ohm------3ohm----
 |(+)      |          |(+)
 12V      2ohm       48V
 |(-)      |          |(-)
 ---------------------
'''
import numpy as np
import numpy as np
branch_equations = np.array([[8,-1,-3], [-1,3,-2], [-3, -2, 5]]) # These are three loop equations
branch_voltages =  np.array([24, 12, 48])
branch_currents = np.linalg.solve(branch_equations,branch_voltages) # Solving the three equations to obtain the current of each loop
# here we formulate the given loop equations into the matrix form of: A = X*B
# And solve it as: X = A*B ^ -1 (A x B inverse)
print('Branch currents are: \n',branch_currents)