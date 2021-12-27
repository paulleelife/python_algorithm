import sys
import numpy as np

input = sys.stdin.readline
n = int(input())

dp = n*[0]
dp[0] = 1

mults = [2, 3, 5] # multipliers
dp_is = 3*[0] # dp indexes of 2, 3, 5

for i in range(1, n):
  while True:
    min_choice = np.argmin([dp[dp_is[0]]*mults[0], 
                            dp[dp_is[1]]*mults[1],
                            dp[dp_is[2]]*mults[2]])
    dp[i] = dp[dp_is[min_choice]]*mults[min_choice]
    dp_is[min_choice] += 1
    if dp[i-1] != dp[i]: break # avoid same numbers

print(dp[-1])
