import numpy as np
import sys

input = sys.stdin.readline

str1 = input()
str2 = input()

# dp table initialize
dp_arr = np.zeros([len(str1)+1, len(str2)+1], dtype=int)
dp_arr[:, 0] = np.arange(len(str1)+1)
dp_arr[0, :] = np.arange(len(str2)+1)

for row in range(1, len(str1)+1):
  for col in range(1, len(str2)+1):
    if str1[row-1] == str2[col-1]:
      dp_arr[row, col] = dp_arr[row-1, col-1]
    else:
      dp_arr[row, col] = 1 + min(dp_arr[row-1, col-1],
                                 dp_arr[row-1, col], 
                                 dp_arr[row, col-1])

print(dp_arr[-1, -1])
