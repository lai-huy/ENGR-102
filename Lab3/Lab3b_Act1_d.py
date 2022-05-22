# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Activity 1d
# Date:         14 SEPTEMBER 2021
#

print("This program calculates the pressure given moles, volume, and temperature")
n = float(input("Please enter the number of moles: "))                  # Amount (mol)
G = 8.314   # Universal Gas Constant (J/K mol)
V = float(input("Please enter the volume (m^3): "))                     # Volume (m^3)
T = float(input("Please enter the temperature (K): "))    # Thermodynamic Temperature (K)
print("Pressure is {:.0f} kPa".format((n * G * T)/(1000 * V)))
