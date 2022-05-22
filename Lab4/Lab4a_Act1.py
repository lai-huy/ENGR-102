# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 4a Activity 1
# Date:         21 SEPTEMBER 2021
#

from math import ceil

# input hours parks
print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
hour = float(input("Please enter the hours parked: "))
hour_float = hour
ticket = False

# determine if ticket was lost
if hour < 0:
    ticket = True
    hour = abs(hour)

# round up to nearest hour
hour = ceil(hour)

# handle parking for over one day
price = (hour // 24) * 24

# force time to be within one day
hour %= 24

# max daily cost
if hour >= 22:
    price += 24
else:
    # loop backwards as each case relies on the case before it
    while hour > 0:
        if hour > 4:
            price += 1
            hour -= 1   # skip over an hour as to not double charge
        elif hour > 2:
            price += 3
            hour -= 2
        else:
            price += 4
            hour -= 2   # skip over an hour as to not double charge

# Lost ticket handling
price += 36 if ticket else 0
print("Parking for {} hours please pay ${:d}".format(hour_float, price))
