# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 11b Activity 1d
# Date:         29 November 2021
#


def partd(file_name):
    """
    Converts a csv to a tsv

    :param file_name: string of file name
    :return: Done!
    """

    # get the name of the file
    base = file_name.split(".")

    # Reader and Writer
    reader = open(file_name, "r")
    writer = open(base[0] + ".tsv", "w")

    # Actual conversion
    for line in reader.readlines():
        writer.write(line.strip().replace(",", "\t"))
        writer.write("\n")

    # Close files
    reader.close()
    writer.close()

    return "Done!"
