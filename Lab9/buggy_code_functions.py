# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Buggy Code Functions
# Date:         26 October 2021
#

# Correct output:
# The median is 67.5
# The mean is 68.52
# The standard deviation is 16.98144870145065

from math import sqrt


def makelist(data):
    # Fake Sort algorithm: add min to new list, remove from old
    # make a copy of gradeData so it's not overwritten
    old_list = data[:]
    new_line = []
    while old_list:
        new_line.append(min(old_list))
        old_list.remove(min(old_list))
    return new_line


def findmedian(n_list):
    # find median value, no need for loops
    if not len(n_list) % 2:
        # even number of elements
        a = (len(n_list) - 1) // 2
        b = a + 1
        return (n_list[a] + n_list[b]) / 2
    else:
        # odd number of elements
        return n_list[(len(n_list) - 1) // 2]


def calcmean(n_list):
    # find mean
    return sum(n_list) / len(n_list)


def calcstdev(n_list, xbar):
    # find standard deviation
    # use population stdev equation: σ = sqrt((Σ(x - mean)^2)/n)
    dev = 0
    for x in n_list:
        dev += (x - xbar) ** 2
    return sqrt(dev / len(n_list))


# grade data list
gradeData = [79, 99, 73, 49, 67, 62, 52, 99, 57, 58, 67, 88, 71, 69, 41, 74, 53, 90, 63, 66, 92, 54, 61, 59, 48, 71, 83,
             89, 99, 69, 66, 40, 48, 41, 99, 68, 52, 78, 77, 71, 40, 65, 77, 87, 96, 44, 54, 60, 89, 72]

# Part A
new_list = makelist(gradeData)

# Part B
median = findmedian(new_list)

# Part C
xbar = calcmean(new_list)
stdev = calcstdev(new_list, xbar)

# print results
print("The median is", median)
print("The mean is", xbar)
print("The standard deviation is", stdev)
