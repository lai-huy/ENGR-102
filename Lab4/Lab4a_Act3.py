# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 4a Activity 3
# Date:         21 SEPTEMBER 2021
#

########### Part A ###########
a = input("Enter True or False for a: ").lower()
b = input("Enter True or False for b: ").lower()
c = input("Enter True or False for c: ").lower()

# Converting
a = True if a == "true" or a == "t" else False
b = True if b == "true" or b == "t" else False
c = True if c == "true" or c == "t" else False

########### Part B ###########
print("a and b and c: {:}".format(a and b and c))
print("a or b or c: {:}".format(a or b or c))

########### Part C ###########
print("XOR: {:}".format((a and not b) or (not a and b)))
print("Odd number: {:}".format((a + b + c) % 2 == 1))

########### Part D ###########
# Expression 1
exp_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)

"""
Boolean Algebra
(~(a~b) + ~cb)(~b) + (~ab~c) + (a~b)    Start
((~a + ~~b + ~cb)~b) + (~ab~c) + (a~b)  DeMorgan
((~a + b + ~cb)~b) + (~ab~c) + a~b      Involution
(~a+b)~b + ~ab~c + a~b                  Absorption
~a~b + b~b + ~ab~c + a~b                Distribution
~a~b + 0 + ~ab~c + a~b                  Compliment
~b(~a+a) + ~ab~c                        Distribution
~b(1) + ~ab~c                           Compliment
~b + ~ab~c                              Identity
~b + ~a~c                               Absorption
"""

# Expression 1 simplified using boolean algebra
sim_1 = not b or (not a and not c)

# Expression 2
exp_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

"""
~((b + ~c)(~a + ~c)) + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))     Start
~(b + ~c) + ~(~a + ~c) + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))   DeMorgan
~b~~c + ~(~a + ~c) + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))       DeMorgan
~bc + ~(~a + ~c) + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))         Involution
~bc + ~~a~~c + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))             DeMorgan
~bc + ac + ~(c + ~(bc)) + (a~c)(~a + abc + a(b~c + ~b))                 Involution x2
~bc + ac + ~c~~(bc) + (a~c)(~a + abc + a(b~c + ~b))                     DeMorgan
~bc + ac + ~cbc + (a~c)(~a + abc + a(b~c + ~b))                         Involution x2
~bc + ac + 0 + (a~c)(~a + abc + a(b~c + ~b))                            Complement
~bc + ac + (a~c)(~a + abc + b~c + ~b)                                   Absorption
~bc + ac + (a~c)(~a + abc + ~c + ~b)                                    Absorption
~bc + a(~c(~a + abc + ~c + ~b) + c)                                     Distributive
~bc + a(~a + abc + ~c + ~b + c)                                         Absorption
~bc + a(~a + abc + ~b + 1)                                              Compliment
~bc + a(1)                                                              Identity
~bc + a                                                                 Identity
"""

# Expression 2 simplified using boolean algebra
sim_2 = (not b and c) or a

# Print
print("Complex 1: {:}".format(exp_1))
print("Complex 2: {:}".format(exp_2))
print("Simple 1: {:}".format(sim_1))
print("Simple 2: {:}".format(sim_2))