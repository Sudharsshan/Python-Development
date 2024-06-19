# This library class calculates the bill amount based on the provided tariff 
# and calculation methods of BESCOM

class BESCOMbill:
    def __init__(self):
        print('BESCOMbill library is used. Constuctor call')
    
    # There are two ways the electricity bill is calculated: 
    # Simple tariff method - bill calculated on fixed price
    # Block tariff method - bill calculated based on units consumed

    def simpleBill(totalLoad, timeConsumed):
        # This method will just calculate the number of units consumed and
        # multiply it with base tariff
        # The base price is set to Rs. 6 per unit
        return (6*(totalLoad/1000)*timeConsumed)

    def commonBill(totalLoad, timeConsumed):
        # This method will calculate the bill as follows
        # first 100 units : Rs. 4.5 / unit
        # Rest units : 7 / unit
        if(totalLoad <= 100):
            billAmount = (totalLoad/1000)*timeConsumed*4.5
        else:
            billAmount = 450 + (totalLoad-100)/1000*timeConsumed*7
        return billAmount