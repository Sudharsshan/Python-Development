from EEE.BESCOMbill import *

# Accept the type of bill
billType = int(input('Please enter 1 or 2 based on type of your bill:\n\n1. Simple bill \n2.Block tariff bill\nYour choice: '))

if(billType == 1 or billType == 2):
    print('Please enter the following details:')
    powerConsumed = int(input('Total power consumed (in Watts): '))
    duration = int(input('Duration of consumption (in hours): '))
    if(billType == 1):
        # Calculate the bill in simple tariff method
        BillAmount = BESCOMbill.simpleBill(powerConsumed, duration)
        print('Bill amount is: Rs.', BillAmount)
    elif(billType == 2):
        # Calculate the bill in block tariff method
        BillAmount = BESCOMbill.commonBill(powerConsumed, duration)
        print('Bill amount is: ', BillAmount)
    # billAmount = BESCOMbill.simpleBill(powerConsumed, duration) if(billType == 1) else BESCOMbill.commonBill(powerConsumed, duration)
    # performs the same operation in single line but looks complex as it uses ternary operation in Python
else:
    print('You have entered incorrect choice, please try again')
print('Thank you')