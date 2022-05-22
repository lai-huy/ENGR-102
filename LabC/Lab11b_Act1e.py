# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1e
# Date:         29 November 2021
#


def parte(data):
    """
    Find the Min, Median, and Max of a data set

    :param data: list of integers
    :return:
    """

    # Sort list
    data.sort()

    # Find the middle of the data set
    middle = len(data) // 2
    if len(data) == 1:
        median = data[0]
    elif len(data) % 2:
        median = data[middle]
    else:
        middle -= 1
        median = (data[middle] + data[middle + 1]) // 2

    # Return
    return min(data), median, max(data)
