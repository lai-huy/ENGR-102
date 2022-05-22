# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 10a Activity 2
# Date:         09 November 2021
#
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

from matplotlib import pyplot as plt
import numpy as np

# Part 1
x = np.linspace(-2, 2)
plt.plot(1 / (4 * 2) * x ** 2, color="blue", linewidth=2)
plt.plot(1 / (4 * 6) * x ** 2, color="red", linewidth=6)
plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Line 0", "Line 1"])
plt.show()

# Part 2
x = np.linspace(-4, 4, num=25)
y = 2 * x ** 3 + 3 * x ** 2 - 11 * x + 6
plt.scatter(x, y, color="yellow", marker="*", edgecolors="black")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plot of cubic polynomial")
plt.show()

# Part 3
x = np.linspace(-2 * np.pi, 2 * np.pi)
X_TICKS = np.arange(-6, 7, 2)
Y_TICKS = np.arange(-1, 2, 1)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle("Plot of cos(x) and sin(x)")

ax1.plot(x, np.cos(x))
ax1.grid(True)
ax1.set_ylabel("y=cos(x)")
ax1.set_xticks(X_TICKS)
ax1.set_yticks(Y_TICKS)

ax2.plot(x, np.sin(x))
ax2.grid(True)
ax2.set_ylabel("y=sin(x)")
ax2.set_xlabel("x")
ax2.set_xticks(X_TICKS)
ax2.set_yticks(Y_TICKS)
plt.show()
