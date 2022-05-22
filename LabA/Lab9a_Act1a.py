# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 9a Activity 1a Final
# Date:         02 November 2021
#

# Keys to make sure the passports have
KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Read from file
reader = open("Lab9a_input.txt", "r")

# Write to file
writer = open("Lab9a_Act1a_valid.txt", "w")

# Reformatted data
data = []
passport = []

# Reformat all data
for line in reader.readlines():
    if line == "\n":
        data.append(passport)
        passport = []
    else:
        spt = line.split(" ")
        for e in spt:
            passport.append(e.strip())
reader.close()

# Convert data to dictionary to check for
for i in range(len(data)):
    line = data[i]
    passport = {}
    for element in line:
        spt = element.split(":")
        passport[spt[0]] = spt[1]
    data[i] = passport

# Counting Time
indexes = []

for i in range(len(data)):
    line = data[i]
    passport = []
    for key in KEYS:
        passport.append(key not in line)
    if not any(passport):
        indexes.append(i)

print(f"There are {len(indexes) + 1} valid passports")

# Write to file time
with open("Lab9a_input.txt", "r") as reader:
    data = reader.read().split("\n\n")

for index in indexes:
    writer.write(data[index] + "\n\n")

writer.close()
