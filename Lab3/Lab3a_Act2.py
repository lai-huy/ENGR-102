# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 3a Activity 2
# Date:         14 SEPTEMBER 2021
#


# List of Variables:
# Input Variables
# t1      int     initial time
# x1      int     initial positions
# y1      int
# z1      int
# t2      int     final time
# x2      int     final positions
# y2      int
# x2      int

# Function Parameters
# ti      int     initial time
# xi      int     initial positions
# yi      int
# zi      int
# tf      int     final time
# xf      int     final positions
# yf      int
# zf      int

# Function Variables
# time    int     difference between initial and final time
# step    float   amount of time to progress by
# vel     list    Velocity in each direction
# t       float   time being calculated
# x       float   new x position at time t
# y       float   new y position at time t
# z       float   new z position at time t

# Description:
# Because velocity = displacement / time
# Therefore displacement = velocity * time
# Because initial position is not guaranteed to be at time = 0,
# these offsets are included in the formula below.
#
# new position = initial position + velocity * (new time - initial time)

# Calculations by hand
# t = 1:
# x = x1 + vel[0] * (t - ti)
# x = 1 + 1 * (1 - 1)
#   = 1
#
# t = 1.25:
# x = x1 + vel[0] * (t - ti)
# x = 1 + 1 * (1.25 - 1)
# x = 1.25

def interpolate(ti, xi, yi, zi, tf, xf, yf, zf):
    time = tf - ti
    step = time / 4
    vel = [(xf - xi) / time, (yf - yi) / time, (zf - zi) / time]
    t, x, y, z = float(ti), float(xi), float(yi), float(zi)
    while t <= tf:
        x = xi + vel[0] * (t - ti)
        y = yi + vel[1] * (t - ti)
        z = zi + vel[2] * (t - ti)
        print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(t, x, y, z))
        t += step
    return


t1 = int(input("Enter time 1: "))
x1 = int(input("Enter the x position of the object at time 1: "))
y1 = int(input("Enter the y position of the object at time 1: "))
z1 = int(input("Enter the z position of the object at time 1: "))
t2 = int(input("Enter time 2: "))
x2 = int(input("Enter the x position of the object at time 2: "))
y2 = int(input("Enter the y position of the object at time 2: "))
z2 = int(input("Enter the z position of the object at time 2: "))
print()
interpolate(t1, x1, y1, z1, t2, x2, y2, z2)
