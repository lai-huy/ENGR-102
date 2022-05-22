# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 6b Activity 1
# Date:         06 October 2021
#

# inputs
n = int(input("Enter a positive integer to compute the Collatz sequence: "))
out = "Here is the Collatz sequence starting at {:d}:"
count = "It took {:d} iterations to reach 1"
numbers = []

print(out.format(n))

# Collatz loop
while n != 1:
    numbers.append(n)
    n = 3 * n + 1 if n % 2 == 1 else n//2

# Append 1 to list
numbers.append(1)

# prints
print(str(numbers)[1:-1])
print(count.format(len(numbers) - 1))
