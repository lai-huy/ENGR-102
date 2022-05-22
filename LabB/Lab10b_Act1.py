# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 10b Activity 1
# Date:         11 November 2021
#

import numpy as np
from matplotlib import pyplot as plt

# Defined Matrix
M = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
v = np.array([1, 0])

# List of points
x_coords = [v[0]]
y_coords = [v[1]]

# Matrix Multiplication
for i in range(250):
    v = M @ v
    x_coords.append(v[0])
    y_coords.append(v[1])


# Split coordinates

plt.plot(x_coords, y_coords, color="black")
plt.grid()

# Display Graph
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spiral")
plt.show()
