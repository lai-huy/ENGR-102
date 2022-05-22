# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 5b Activity 2
# Date:         30 SEPTEMBER 2021
#

# Constants
E = 4300    # Young's Modulus
m_BC = 10
m_CD = 137.5
m_DE = -100
out_str = "The stress is approximately {:.1f}"

# Input
stress = float(input("Enter the strain: "))

# Output
strain = 0

# from O to A
if 0 <= stress < .01:
    strain = E * stress

# from A to C
elif .01 <= stress < .06:
    strain = m_BC * (stress - .01) + 43

# from C to D
elif .06 <= stress < .18:
    strain = m_CD * (stress - .06) + 43.5

# from D to E
elif .18 <= stress <= .27:
    strain = m_DE * (stress - .18) + 60

# Outside Domain
else:
    print("Strain is undefined in that region")
    exit(0)
print(out_str.format(strain))
