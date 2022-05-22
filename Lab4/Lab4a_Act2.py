# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 4a Activity 2
# Date:         21 SEPTEMBER 2021
#

#inputs
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

# Strings to add
x = "x"
x2 = "x^2"
plus = " + "
minus = " - "
negative = "- "
equal_0 = " = 0"

#output
out = ""

# determining if a is zero
if a != 0:
    if a < 0:
        out += negative
    if abs(a) != 1:
        out += str(abs(a))
    out += x2

# determining if b is zero
if b != 0:
    out += minus if b < 0 else plus
    if abs(b) != 1:
        out += str(abs(b))
    out += x

# determining if c is zero
if c != 0:
    out += minus if c < 0 else plus
    if abs(c) != 1:
        out += str(abs(c))

# Adding " = 0"
out += equal_0

# Post-processing string to remove leading " + " and alter " - ".
if out[0:3] == plus:
    out = out[3:]
elif out[0:3] == minus:
    out = out[1:]

#print time
print("The quadratic equation is {:s}".format(out))
