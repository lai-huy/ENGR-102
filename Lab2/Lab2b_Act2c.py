# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY QUANG LAI 132000359
# Section:      ENGR-102-569
# Assignment:   Lab 2b Activity 2c
# Date:         06 SEPTEMBER 2021
#

p1 = [2, 3, 7]      # Position 1
t1 = 12             # Time 1
p2 = [25, -5, 11]   # Position 2
t2 = 85             # Time 2

disp = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]    # Displacement
time = t2 - t1                                          # Time it took
vel = [disp[0]/time, disp[1]/time, disp[2]/time]        # Velocity

start = 30
end = 60
step = (end - start)/4
t = float(start)

while t <= end:
    p0 = [p1[0] + vel[0] * (t - t1), p1[1] + vel[1] * (t - t1), p1[2] + vel[2] * (t - t1)]   # Position given time
    print("At time", t, "seconds:")
    print("x0 =", p0[0], "m")
    print("y0 =", p0[1], "m")
    print("z0 =", p0[2], "m")
    if t != end:
        print("----------------------")
    t += step