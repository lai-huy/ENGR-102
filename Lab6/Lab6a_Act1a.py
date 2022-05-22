# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 6a Activity 1a
# Date:         04 October 2021
#

n = float(input("Enter the side length in meters: "))
layer = int(input("Enter the number of layers: "))
out = "You need {:.2f} square meters of gold foil to cover the pyramid"

area = 0

# loop from first layer to last layer including last layer
for i in range(layer):
    area += ((i + 1) * n) ** 2 - (i * n) ** 2   # Top Square excluding square covered by previous layer
    area += (4 * (i + 1)) * n ** 2                    # Sides

# Print time
print(out.format(area))
