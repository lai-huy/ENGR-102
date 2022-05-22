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
EYE = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# Read from file
reader = open("Lab9a_input.txt", "r")

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

# Validation
temp = []

# Check for keys, this automatically causes a passport to be invalid
for line in data:
    passport = {}
    for key in KEYS:
        passport[key] = key not in line
    temp.append(passport)

# Check each individual aspect
for i in range(len(temp)):
    line = data[i]
    t_ln = temp[i]
    if any(list(t_ln.values())):
        pass
    else:
        t_ln["byr"] = not ("1920" <= line["byr"] <= "2005")
        t_ln["iyr"] = not ("2011" <= line["iyr"] <= "2021")
        t_ln["eyr"] = not ("2021" <= line["eyr"] <= "2031")

        unit = line["hgt"][-2:]
        hgt = line["hgt"][:-2]
        valid_hgt = False
        if unit == "in":
            valid_hgt = "59" <= hgt <= "76"
        elif unit == "cm":
            valid_hgt = "150" <= hgt <= "193"
        t_ln["hgt"] = not valid_hgt

        valid_hcl = False
        if line["hcl"][0] == "#":
            if len(line["hcl"][1:]) == 6:
                try:
                    int(line["hcl"][1:], 16)
                    valid_hcl = True
                except ValueError as ve:
                    valid_hcl = False
        t_ln["hcl"] = not valid_hcl

        t_ln["ecl"] = line["ecl"] not in EYE

        valid_pid = False
        if len(str(line["pid"])) == 9:
            valid_pid = line["pid"].isdigit()
        t_ln["pid"] = not valid_pid

# Counting Time
indexes = []

for i in range(len(temp)):
    line = list(temp[i].values())
    if not any(line):
        indexes.append(i)

# print
print(f"There are {len(indexes) + 1} valid passports")

with open("Lab9a_input.txt", "r") as reader:
    data = reader.read().split("\n\n")

# Write to file
with open("Lab9a_Act1b_valid.txt", "w") as writer:
    for index in indexes:
        writer.write(data[index] + "\n\n")
