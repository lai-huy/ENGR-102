# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1f
# Date:         29 November 2021
#


def partf(times, distances):
    """
    Calculates average velocities between times and distances

    :param times: list of times
    :param distances: list od distances
    :return: list of velocities
    """

    # Empty list
    vel = []

    # Calculates velocities
    for i in range(len(times) - 1):
        vel.append((distances[i + 1] - distances[i])/(times[i + 1] - times[i]))

    return vel
