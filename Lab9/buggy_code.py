# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Buggy Code
# Date:         26 October 2021
#

# Correct output:
# The median is 67.5
# The mean is 68.52
# The standard deviation is 16.98144870145065

from math import sqrt
# grade data list
gradeData = [79, 99, 73, 49, 67, 62, 52, 99, 57, 58, 67, 88, 71, 69, 41,
             74, 53, 90, 63, 66, 92, 54, 61, 59, 48, 71, 83, 89, 99, 69,
             66, 40, 48, 41, 99, 68, 52, 78, 77, 71, 40, 65, 77, 87, 96,
             44, 54, 60, 89, 72]

# Part A
# Fake Sort algorithm: add min to new list, remove from old
# make a copy of gradeData so it's not overwritten
oldlist = gradeData[:]
newlist = []

while oldlist:
    newlist.append(min(oldlist))
    oldlist.remove(min(oldlist))

# Part B
# find median value, no need for loops
if not len(newlist) % 2:
    # even number of elements
    a = (len(newlist) - 1) // 2
    b = a + 1
    median = (newlist[a] + newlist[b]) / 2
else:
    # odd number of elements
    median = newlist[(len(newlist) - 1) // 2]

# Part C
# find mean and standard deviation
# use population stdev equation: σ = sqrt((Σ(x - mean)^2)/n)
xbar = sum(newlist) / len(newlist)
dev = 0
for x in newlist:
    dev += (x - xbar) ** 2
dev = sqrt(dev / len(newlist))

# print results
print("The median is", median)
print("The mean is", xbar)
print("The standard deviation is", dev)
