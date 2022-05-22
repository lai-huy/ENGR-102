# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1b
# Date:         29 November 2021
#


def partb(names, costs, values):
    """
    Returns the most profitable name and its profit

    :param names: list of names
    :param costs: list of costs
    :param values: list of values
    :return: most profitable name
    """

    # Net profit
    net = [0] * len(names)
    max_profit = -1
    index = -1

    # Loop through the data
    for i in range(len(names)):
        net[i] = values[i] - costs[i]
        if net[i] > max_profit:
            max_profit = net[i]
            index = i

    return names[index], max_profit
