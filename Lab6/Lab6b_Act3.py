# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 6a Activity 3
# Date:         06 October 2021
#

n = int(input("Enter a four-digit integer: "))
number = n
out_list = []
out_str = "{:d} reaches {:d} via Kaprekar's routine in {:d} iterations"

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

    if not number:
        out_list.append(0)
        break

if not len(out_list) or out_list[-1]:
    out_list.append(6174)

print(*out_list, sep=" > ")
print(out_str.format(n, 6174 if out_list[-1] else 0, len(out_list) - 1))
