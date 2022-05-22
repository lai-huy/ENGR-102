import numpy as np

# Open File to read
with open("module11activity.txt", "r") as reader:
    data = reader.readlines()

# Convert to 100 by 100 matrix
x = 0
y = 0
matrix = np.zeros([100, 100], np.int32)
for line in data:
    matrix[x, y] = int(line.strip())
    x += 1
    if x == 100:
        x %= 100
        y += 1

key = sum(matrix[5][5:]) << 1
key += int(sum(matrix[24])/100)
# key += 15
# key 87

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in matrix:
    count[i[74] - 1] += 1

mode = 0
index = -1
for i in range(len(count)):
    if count[i] > mode:
        mode = count[i]
        index = i

key += index
# key += 1
print(key, key % 26)

message = "xjhwjymzqqfgfqtt"

out = []
for c in message:
    out.append(chr(ord(c) - key % 26))
print("".join(out))
