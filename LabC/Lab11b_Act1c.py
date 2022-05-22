# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1c
# Date:         29 November 2021
#


def partc(name, city, state, ZIP, address):
    """
    Formats inputs with the postal format.
    
    :param name: name of person
    :param city: city of residence
    :param state: state of residence
    :param ZIP: ZIP code of residence
    :param address: address of residence
    :return: format string
    """

    # Format
    return f"{name}\n{address}\n{city}, {state} {ZIP}"
