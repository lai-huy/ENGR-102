# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 6a Activity 3 Challenge
# Date:         06 October 2021
#

master_list = []

for n in range(1, 10000):
    number = n
    out_list = []
    out_str = "{:d} reaches 6174 via Kaprekar's routine in {:d} iterations"

    while number != 6174:
        out_list.append(number)

        # Add leading zeros if necessary
        num = str(number)
        while len(num) < 4:
            num = "0" + num

        # Sort digits
        dsc = [str(x) for x in num]
        dsc.sort(reverse=True)
        asc = [str(x) for x in num]
        asc.sort(reverse=False)

        # Convert lists to numbers
        number = int("".join(dsc)) - int("".join(asc))

        # Check for zero
        if not number:
            out_list.append(0)
            break

    if not len(out_list) or out_list[-1]:
        out_list.append(6174)

    master_list.append(len(out_list) - 1)

print("Kaprekar's routine takes {:d} total iterations for all four-digit numbers".format(sum(master_list)))
