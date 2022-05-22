# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 7b Activity 1
# Date:         14 October 2021
#

# Input
name = input("What is your name? ")

# all consonants
consonants = "bcdfghjklmnpqrstvwxyz"

# Get rhyming syllable
n = list(name)

# Remove all consonants
while n[0].lower() in consonants:
    n = n[1:]

# Fix capitalization
n[0] = n[0].lower()

# Back to String
n = "".join(n)

# Print awesome rhyme
print("{0:s}, {0:s}, Bo-B{1:s}".format(name, n))
print("Banana-Fana Fo-F{:s}".format(n))
print("Me Mi Mo-M{0:s}".format(n))
print("{:s}!".format(name))
