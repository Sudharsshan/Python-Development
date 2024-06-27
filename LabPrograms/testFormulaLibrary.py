'''
Date: 10-06-2024
TASK: Write a program to test the funcitons created in basicFormulas custom library
'''

from EEE.basicFormulas import *

# Loop the user through a for loop asking for the required calculation
loopVariable = True

while(loopVariable):
    print('\nPlease enter the following number for the respective calculation')
    print('1 Voltage\n2 Active Power\n3 Reactive Power\n4 Impedance Magnitude\n5 Energy\n6 Exit')
    UserChoice = int(input('Your choice: '))
    
    match UserChoice:
        case 1: 
            # Calculate voltage
            resistance = float(input('Please enter resistance: '))
            current = float(input('Please input current: '))
            voltage = basicFormulas.Voltage(resistance, current)
            print("Voltage = ", voltage, "V")

        case 2:
            # Calculate active power
            voltage = float(input('Please enter voltage: '))
            current = float(input('Please input current: '))
            powerFactor = float(input('Please input power factor (cos): '))
            activePower = basicFormulas.ActivePower(voltage, current, powerFactor)
            print("Active power consumed = ", activePower,"W")
            
        case 3:
            # Calculate reactive power
            voltage = float(input('Please enter voltage: '))
            current = float(input('Please input current: '))
            powerFactor = float(input('Please input power factor (sin): '))
            reactivePower = basicFormulas.ReactivePower(voltage, current, powerFactor)
            print("Reactive power consumed = ", reactivePower,"W")

        case 4:
            # Calculate Impedance
            resistance = float(input('Please enter resistance: '))
            inductiveReactance = float(input('Please input inductive reactance: '))
            capacitiveReactance = float(input('Please input capacitive reactance: '))
            impedance = basicFormulas.ImpedanceMagnitude(resistance, inductiveReactance, capacitiveReactance)
            print("Impedance magnitude = ", impedance,"Ω")

        case 5:
            # Calculate energy consumed
            power = float(input('Please enter power consumed: '))
            time = float(input('Please input time: '))
            energy = basicFormulas.Energy(power, time)
            print("Energy consumed = ", energy,"Wh")

        case 6:
            # Exit the loop
            print('Thank you')
            loopVariable = False