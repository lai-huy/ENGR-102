# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 7a Activity 1a
# Date:         12 October 2021
#

from colorama import Fore, Style

# Constants
blank = "."

# Pieces
red = Fore.RED + Style.BRIGHT + chr(9920) + Fore.RESET + Style.NORMAL
black = Fore.BLACK + Style.BRIGHT + chr(9922) + Fore.RESET + Style.NORMAL

FROM = "Input a square to move from: "
TO = "Input a square to move to: "

# Actual board
board = [list(blank * 8),
         list(blank * 8),
         list(blank * 8),
         list(blank * 8),
         list(blank * 8),
         list(blank * 8),
         list(blank * 8),
         list(blank * 8)
         ]

# Hardcoded to not allow movement to white squares
coords = [
    (0, 1), (0, 3), (0, 5), (0, 7),
    (1, 0), (1, 2), (1, 4), (1, 6),
    (2, 1), (2, 3), (2, 5), (2, 7),
    (3, 0), (3, 2), (3, 4), (3, 6),
    (4, 1), (4, 3), (4, 5), (4, 7),
    (5, 0), (5, 2), (5, 4), (5, 6),
    (6, 1), (6, 3), (6, 5), (6, 7),
    (7, 0), (7, 2), (7, 4), (7, 6),
]


def reset(b: list[list]) -> None:
    """
    Reset the checker board

    :param b: board to reset
    :return: nothing
    """

    # remove all pieces
    for row in range(len(b)):
        for col in range(len(b[row])):
            b[row][col] = blank

    # Place all black pieces
    for i in range(1, 13):
        coord = to_index(i)
        board[coord[0]][coord[1]] = black

    # Place all red pieces
    for i in range(21, 33):
        coord = to_index(i)
        board[coord[0]][coord[1]] = red


def print_board(b: list[list]):
    """
    prints board to console with formatting

    :param b: board
    :return: nothing
    """

    # loop through the whole board
    for row in b:
        for col in row:
            print(col, end="")
        print()


def to_index(n: int) -> tuple[int, int]:
    """
    Converts a single int to an index in the board

    :param n: number ot convert
    :return: coordinate (row, col)
    """

    # Hardcoded so can't move to white spaces
    return coords[n - 1]


# Main game loop
reset(board)
while True:
    # Print board
    print_board(board)

    # Move from
    try:
        foo = int(input())
        while foo > 32 or foo < 0:
            foo = int(input(FROM))
    except ValueError:
        exit(0)

    origin = to_index(foo)

    # Can not move empty
    while board[origin[0]][origin[1]] == blank:
        print("Empty square!")

        try:
            foo = int(input(FROM))
            while foo > 32 or foo < 0:
                foo = int(input(FROM))
        except ValueError:
            exit(0)

    # Move To
    try:
        foo = int(input(TO))
        while foo > 32 or foo < 0:
            foo = int(input(TO))
    except ValueError:
        exit(0)

    new = to_index(foo)

    # Move Pieces
    board[new[0]][new[1]] = board[origin[0]][origin[1]]
    board[origin[0]][origin[1]] = blank
