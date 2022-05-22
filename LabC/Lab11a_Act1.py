# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 11a Activity 1
# Date:         16 November 2021

def readfile(file: str):
    """
    Reads from a file and returns a list of points.
    Each element in the list of points should itself be a list of one point.

    :param file: File name
    :return: list of points
    """

    # Create a file reader
    with open(file, "r") as reader:
        pts = []

        # Split file into a list
        lines = reader.readlines()

        # Exclude first line because it holds column names
        for line in lines[1:]:
            pts.append([int(i) for i in line.strip().split(',')])

        return pts


def cross(a, b):
    """
    Despite this method's name, calculate the determinant of two points.

    :param a: first point
    :param b: second point
    :return: determinant of the points
    """

    return a[0] * b[1] - a[1] * b[0]


def shoelace(points):
    """
    Performs the shoelace algorithm.
    Takes the sum of all determinants between two consecutive points divided by 2

    :param points: list of points
    :return: the area of the polygon
    """

    areas = []

    # Loop through points and cross product with neighbor
    for i in range(len(points)):
        areas.append(cross(points[i - 1], points[i]))

    return sum(areas) / 2


def main() -> None:
    """
    Main method

    :return: None
    """

    points = readfile(input("Please enter the filename: "))
    print(f"The area of the polygon is {shoelace(points):.1f}")


# Execute main()
if __name__ == "__main__":
    main()
