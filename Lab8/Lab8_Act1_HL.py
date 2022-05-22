# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 8 Activity 1 Final
# Date:         19 October 2021
#

# Data from file
data = [
    [0.0009977, 0000.04, 0005.03, 0.0001],
    [0.0009996, 0083.61, 0088.61, 0.2954],
    [0.0010057, 0166.92, 0171.95, 0.5705],
    [0.0010149, 0250.29, 0255.36, 0.8287],
    [0.0010267, 0333.82, 0338.96, 1.0723],
    [0.0010410, 0417.65, 0422.85, 1.3034],
    [0.0010576, 0501.91, 0507.19, 1.5236],
    [0.0010769, 0586.80, 0592.18, 1.7344],
    [0.0010988, 0672.55, 0678.04, 1.9374],
    [0.0011240, 0759.47, 0765.09, 2.1338],
    [0.0011531, 0847.92, 0853.68, 2.3251],
    [0.0011868, 0938.39, 0944.32, 2.5127],
    [0.0012268, 1031.60, 1037.70, 2.6983],
    [0.0012755, 1128.50, 1134.90, 2.8841]
]

# input temperature
T = float(input("Enter a temperature between 0 and 260 deg C: "))

# Scale temperature to index file
T_scaled = int(T // 20)

if T >= 260:
    T_scaled -= 1

# Unscaled T rounded to closest multiple of 20
T_unscaled = 20 * T_scaled