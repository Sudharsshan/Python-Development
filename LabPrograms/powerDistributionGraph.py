# Date: 26-06-24
# Write a program to visualize the power distribution where input power is given 
# to the highest paying consumer of the two

import matplotlib.pyplot as plt
import numpy as np

consumer1_cost = [10, 5, 7, 6, 12]
consumer2_cost = [11, 9, 10, 12, 8]
consumer1_usedPower = [0]*5
consumer2_usedPower = [0]*5

for i in range(0, 5):
    if(consumer1_cost[i]<consumer2_cost[i]):
        consumer2_usedPower[i] = consumer2_cost[i]
        consumer1_usedPower[i] = 0
    else:
        consumer2_usedPower[i] = 0
        consumer1_usedPower[i] = consumer1_cost[i]

print('Power given to consumer 1: ',consumer1_usedPower)
print('Power given to consumer 2: ',consumer2_usedPower)

# Plot the graphs for power input, power given to consumer 1 & 2
plt.subplot(4,1,1)
plt.plot(range(0,5), consumer1_cost)
plt.xlabel('time')
plt.ylabel('Power cost payed')
plt.title('Consumer 1 power')

plt.subplot(4,1,2)
plt.plot(range(0,5), consumer2_cost)
plt.xlabel('time')
plt.ylabel('Power cost payed')
plt.title('Consumer 2 power')


plt.subplot(4,1,3)
plt.plot(range(0,5), consumer1_usedPower)
plt.xlabel('time')
plt.ylabel('Power cost payed')
plt.title('Consumer 1 obtained power')

plt.subplot(4,1,4)
plt.plot(range(0,5), consumer2_usedPower)
plt.xlabel('time')
plt.ylabel('Power cost payed')
plt.title('Consumer 2 obtained power')
plt.show()