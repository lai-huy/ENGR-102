# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY QUANG LAI 132000359
# Section:      ENGR-102-569
# Assignment:   Lab 2b Activity 1
# Date:         06 SEPTEMBER 2021
#

import math

# Part A
mass = 5            # mass (kg)
accl = 2            # acceleration (m/s^2)
force = mass * accl # force (kgm/s^2, N)
print("Force is", force, "N")

# Part B
d       = .025              # distance (nm)
theta   = 25 * math.pi/180  # angle (rad)
print("Wavelength is", 2 * d * math.sin(theta), "nm")

# Part C
N0      = 3     # Initial amount (g)
t       = -5    # Amount of time has passed (days)
t_half  = 3.8   # Half-life (days)
print("Radon-222 left is", N0 * 2 ** (t/t_half), "g")

# Part D
n = 5       # Amount (mol)
G = 8.314   # Universal Gas Constant (J/K mol)
T = 425     # Thermodynamic Temperature (K)
V = .15     # Volume (m^3)
print("Pressure is", (n * G * T)/(1000 * V), "kPa")
