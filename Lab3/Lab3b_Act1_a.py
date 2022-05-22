# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Activity 1a
# Date:         14 SEPTEMBER 2021
#

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))               # Mass (kg)
accl = float(input("Please enter the acceleration (m/s^2): "))    # acceleration (m/s^2)
print("Force is {:.1f} N".format(mass * accl))
