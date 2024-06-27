# Date: 27-06-24
# Write a python program to optimise the power distribution for maximum profit.
# Use linear optimization in scipy for the same
# This module extends the previous module 'powerDistributionOptimization.py' and uses the given values
# to calculate the requirements

from scipy.optimize import linprog
generationCost = [4,7] # generator 1 cost, generator 2 cost
powerDeliveredByGen = [[1,1]] # generator 1 power delivered; generator 2 power delivered **
totalPowerRequired= [20] # This is the total power required
gen1_powerLimits = (3,12) # min and max power generation power limits of gen 1
gen2_powerLimits = (5, 10) # min and max power generation power limits of gen 2
res = linprog(generationCost, A_eq=powerDeliveredByGen, b_eq=totalPowerRequired, bounds=[gen1_powerLimits, gen2_powerLimits])
# Here A_eq and B_eq are equality constants because in the equaiton A=XB the equation uses equality constant
# Here A_ub and B_ub are the unequality constrains for the equation when the bounds of the equations are unknown
print("Total cost of generation: ",res.fun)
print("Power distributed among generators: ",res.x)

# ** - in this line we use [[1,1]] because they form the coefficeints of the power generated 
# in the equation A = X*B wherein A is the power generated