# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 9b Activity 2
# Date:         04 November 2021
#

# Inputs
out_file_name = input("Please enter the output filename: ")
P = int(input("Please enter the principal amount: "))
N = int(input("Please enter the term length (months): "))
i = float(input("Please enter the annual interest rate: "))

# Calculations
J = i/12
M = (P * J)/(1 - (1/(1+J))**N)

# Write to file
writer = open(out_file_name, "w")
writer.write("Month,Total Accrued Interest,Loan Balance\n")
writer.write(f"0,$0.00,${P:.2f}\n")

bal = P
INT = 0

for n in range(1, N + 1):
    INT += bal * J
    bal = bal * (1 + J) - M
    if bal < 0:
        bal = 0
    writer.write(f"{n},${INT:.2f},${bal:.2f}\n")

writer.close()
