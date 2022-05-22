# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 9b Activity 1
# Date:         04 November 2021
#

# Read from file
reader = open("game.txt", "r")

# Write to file
writer = open("coins.txt", "w")

# Read data
data = reader.read().split("\n")
coin = 0

# loop through file
index = 0
while True:
    if index >= len(data):
        break
    line = data[index]
    op = line.split(" ")
    if op[0] == "coin":
        amount = int(op[1])
        coin += amount
        writer.write(str(amount))
        writer.write("\n")
        index += 1
    elif op[0] == "jump":
        index += int(op[1])
    else:
        index += 1

print(f"Total coins: {coin}")
