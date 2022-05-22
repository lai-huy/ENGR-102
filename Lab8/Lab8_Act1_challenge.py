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

# input temperature
T = float(input("Enter a temperature between 0 and 260 deg C: "))
P = float(input("Enter a pressure between 5 and 10 MPa: "))

# Data from file
data_0 = [
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

data_1 = [
    [0.0009952, 0000.12, 0010.07, 0.0003],
    [0.0009973, 0083.31, 0093.28, 0.2943],
    [0.0010035, 0166.33, 0176.37, 0.5685],
    [0.0010127, 0249.43, 0259.55, 0.8260],
    [0.0010244, 0332.69, 0342.94, 1.0691],
    [0.0010385, 0416.23, 0426.62, 1.2996],
    [0.0010549, 0500.18, 0510.73, 1.5191],
    [0.0010738, 0584.72, 0595.45, 1.7293],
    [0.0010954, 0670.06, 0681.01, 1.9316],
    [0.0011200, 0756.48, 0767.68, 2.1271],
    [0.0011482, 0844.32, 0855.80, 2.3174],
    [0.0011809, 0934.01, 0945.82, 2.5037],
    [0.0012192, 1026.20, 1038.30, 2.6876],
    [0.0012653, 1121.60, 1134.30, 2.8710]
]

data = data_0

# Combine data with inputted pressure
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = ((data_1[i][j] - data_0[i][j]) / 5) * (P - 5) + data_0[i][j]

# Scale temperature to index file
T_scaled = int(T // 20)

if T >= 260:
    T_scaled -= 1

# Unscaled T rounded to closest multiple of 20
T_unscaled = 20 * T_scaled

# Get all necessary data
val = data[T_scaled]

# Next row values
val_next = data[T_scaled + 1]

# Calculate Slope for volume
slope = [(i - j) / 20 for i, j in zip(val_next, val)]

# Specific volume calculation
vol = slope[0] * (T - T_unscaled) + val[0]
eng = slope[1] * (T - T_unscaled) + val[1]
ehp = slope[2] * (T - T_unscaled) + val[2]
ety = slope[3] * (T - T_unscaled) + val[3]

# Epic print
print(f"Properties at {T} deg C and {P} MPa are:")
print(f"Specific volume (m^3/kg): {vol:.7f}")
print(f"Specific internal energy (kJ/kg): {eng:.2f}")
print(f"Specific enthalpy (kJ/kg): {ehp:.2f}")
print(f"Specific entropy (kJ/kgK): {ety:.4f}")
