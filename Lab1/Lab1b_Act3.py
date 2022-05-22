# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY QUANG LAI 132000359
# Section:      ENGR-102-569
# Assignment:   Lab 1b Activity 3
# Date:         31 AUGUST 2021
#

import math as m

print("This shows the evaluation of (e^x-1)/x evaluated close to x=0")
print("My guess is 1")

for x in [1,.1,.01,.001,.0001,.00001,.000001,.0000001]:
    print((m.exp(x) - 1) / x)

print("")
print("My guess was correct")