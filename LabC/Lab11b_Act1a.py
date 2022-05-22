# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1a
# Date:         29 November 2021
#

from math import pi, asin


def parta(length, width, height, radius):
    """
    Calculates the volume of a cuboid that has a cylindrical hole drilled through it

    :param length: length of box
    :param width: width of box
    :param height: height of box
    :param radius: radius of cylinder
    :return: volume
    """

    # Radius is too big
    if radius > min(length/2, width/2):
        # Angle of sector in the top right corner
        gamma = asin(min(length/2, width/2)/radius)

        # Figure this out

        # Subtract four times this area from the box
        area = (width * height - 2 * gamma * radius ** 2) * height

    # Normal Radius size
    else:
        # Box Volume
        box_vol = length * width * height

        # Cylinder Volume
        cyl_vol = pi * radius ** 2 * height

        # total Area
        area = box_vol - cyl_vol

    return area if area > 0 else 0
