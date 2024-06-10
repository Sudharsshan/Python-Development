# This library consists of basic electrical formulas

import math
class basicFormulas:
    
    # return voltage based on given resistance and current
    def Voltage(r, i):
        # Provide resistance in Ohms and current in Amps
        return r*i
    
    # return Active power based on given voltage, current and power factor
    def ActivePower(v, i, sinph):
        # Provide voltage in Volts, current in Amps and sinph in Degrees
        return v*i*sinph
    
    # return Reactive power based on given voltage, current and power factor
    def ReactivePower(v, i, cosph):
        # Provide voltage in Volts, current in Amps and cosph in Degrees
        return v*i*cosph
    
    # return Impedance magnitude based on given resistance, inductive reactance and capacitive reactance
    def ImpedanceMagnitude(resistance, inductiveReactance, capacitiveReactance):
        # Provide resistance, inductive reactance and capacitive reactance in Ohms
        return math.sqrt(resistance*resistance + (inductiveReactance + capacitiveReactance)**2)
    
    # return Energy based on given power consumed and time taken
    def Energy(power, time):
        # Provide power in Watts and time in Seconds
        return power*time