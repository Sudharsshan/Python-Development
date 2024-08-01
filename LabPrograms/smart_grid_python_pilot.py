'''
TASK: Write a python program to develop a smart grid system to monitor peak load management
'''

# sample output:
'''
Please enter the daily power consumed for a week (in Watts): 450, 600, 250, 400, 372, 470, 640

BESCOM's power limits per customer per week: 3kW

Total power consumed (in kWh): YYYY.YY kWh

==========================WARNING==========================
You've exceeded the customer power limit.

Excess power consumed: EEE kW

Loss to be beared by the company due to user (Rs.200 per 500 Watts): Rs.RRR
Fine to be paid by the consumer (20% of company's loss): Rs. WWW
'''

# take user input for a week's power consumption
weeklyPowerConsumed = [0]*7

print("Please enter the daily power consumed for a week (in Watts):")
for i in range(7):
    weeklyPowerConsumed = int(input())

# calculate the total power consumed

totalPower = 0 # setting initial power consumption to 0 Watts
for i in range(7):
    totalPower = totalPower + weeklyPowerConsumed

BESCOM_powerLimits = 3000 # in Watts

excessPower = 0 # initially no excess power consumed
companyLoss = 0 # initially no losses faced by company
userFine = 0 # no initial fine to be paid by the consumer
finalBill = 0 # initial bill amount is Rs.0

if(totalPower > BESCOM_powerLimits):
    # calculate the excess power consumed by the user
    excessPower = totalPower - BESCOM_powerLimits

    # calculate the losses to be beared by the company
    companyLoss = excessPower/500 * 200

    # calculate the fine to be paid by the user
    userFine = 0.2 * companyLoss

if(totalPower < BESCOM_powerLimits):
    # calculate the excess power remaining
    excessPower = totalPower - BESCOM_powerLimits

    # company pays back consumer a certain amount i.e. 0.08% of bill amount
    userFine = -0.08 * excessPower

if(excessPower > 0):
    # consumer has to pay fine
    print("==========================WARNING==========================\nYou've exceeded the customer power limit.")
    print(f"Excess power consumed: {excessPower} W")
    print(f"Loss to be beared by the company due to user (Rs.200 per 500 Watts): Rs.{companyLoss}")
    print(f"Fine to be paid by the consumer (20% of company's loss): Rs.{userFine}")

elif(excessPower < 0):
    print("==========================CONGRADULATIONS==========================\nYou've NOT exceeded the customer power limit.")
    print("Therefore you are given a certain concession for the bill amount.")

# calculate the final bill amount
finalBill = userFine + totalPower*3

print(f"total power: {totalPower}")
print("=========================FINAL BILL AMOUNT========================")
print(f"Bill amount: Rs.{finalBill}")