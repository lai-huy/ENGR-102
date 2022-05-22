# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 4b Activity 2
# Date:         23 SEPTEMBER 2021
#

########### Part A ##########
a = 1 / 7
print("a = {}".format(a))
b = a * 7
print("b = a * 7 = {}".format(b))

# With no round off, b would be exactly 1

c = 2 * a
d = 5 * a
f = c + d
print("f = 2 * a + 5 * a = {}".format(f))

# With no round off, f would be exactly 1

from math import sqrt
x = sqrt(1 / 3)
print("x = {}".format(x))
y = x * x * 3
print("y = x * x * 3 = {}".format(y))
z = x * 3 * x
print("z = x * 3 * x = {}".format(z))

# With no round off both y and z would be exactly 1
########### Part B ##########

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL:
    print("b and f are equal within tolerance of {}".format(TOL))
else:
    print("b and f are NOT equal within tolerance of {}".format(TOL))

# check if y and z are equal within specified tolerance
if abs(y - z) < TOL:
    print("y and z are equal within tolerance of {}".format(TOL))
else:
    print("y and z are NOT equal within tolerance of {}".format(TOL))

########### Part C ##########
m = 0.1
print("m = {}".format(m))
n = 3 * m
print("n = 3 * m = 0.3 {}".format(n == 0.3))
p = 7 * m
print("p = 7 * m = 0.7 {}".format(p == 0.7))
q = n + p
print("q = 1 {}".format(q == 1))
