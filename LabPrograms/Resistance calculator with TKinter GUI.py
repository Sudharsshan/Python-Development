# DATE: 08-08-2024
# TASK: develop a python application to accept voltage and current to find resistance.
#       Utilize TKinter library to develop a minimal GUI for the same

# in TKinter rooms are like pages within a website or screens in any other GUI
import tkinter as tk

def OhmsLaw():
    v = float(entryVoltage.get())
    i = float(entryCurrent.get())
    r = v/i
    label_r.insert(0, f"{r} Ohm")

root = tk.Tk()
root.title("Basic electrical calci")
root.geometry("400x400")

label_v = tk.Label(root, text="Voltage:")
label_v.grid(row=0, column=0, padx=10, pady=5)

entryVoltage = tk.Entry(root)
entryVoltage.grid(row=0, column=1, padx=10, pady=5)

label_i = tk.Label(root, text="Current:")
label_i.grid(row=1, column=0, padx=10, pady=5)

entryCurrent = tk.Entry(root)
entryCurrent.grid(row=1, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=OhmsLaw)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

resistanceLabel = tk.Label(root, text= "Resistance:")
resistanceLabel.grid(row=2, column=0, padx=10, pady=5)

label_r = tk.Entry(root)
label_r.grid(row=2, column=1, columnspan=2, pady=5)

# ====================== CUSTOM IMPLEMENTATION ========================
# Calculate power:

# calculate the power
def powerCalculation():

    # fetch the values from 'Voltage' and 'Current' boxes
    v = float(voltageBox.get())
    i = float(currentBox.get())
    
    # calculate the power
    power = v*i
    
    # display the power in 'Power' box
    powerBox.insert(0, f"{power} Watts")

# Input voltage Label
voltageLable = tk.Label(root, text="Voltage: ")
voltageLable.grid(row=4, column=0, padx= 10, pady=15)

# Input voltage box
voltageBox = tk.Entry(root)
voltageBox.grid(row=4, column=1, padx=10, pady=15)

# Input current Label
currentLable = tk.Label(root, text="Current: ")
currentLable.grid(row=5, column=0, padx= 10, pady=15)

# Input current box
currentBox = tk.Entry(root)
currentBox.grid(row=5, column=1, padx=10, pady=15)

# button to initiate calculation of power
power_button = tk.Button(root, text="Calculate", command=powerCalculation)
power_button.grid(row=6, column=1, columnspan=2, pady=10)

# Input voltage Label
powerLabel = tk.Label(root, text="Power: ")
powerLabel.grid(row=7, column=0, padx= 10, pady=15)

# Show power consumed ot the user in this box
powerBox = tk.Entry(root)
powerBox.grid(row=7, column=1, padx=10, pady=15)

root.mainloop()