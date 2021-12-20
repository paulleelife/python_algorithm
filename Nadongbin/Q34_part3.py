import sys

input = sys.stdin.readline

N = int(input())
Ps = list(map(float, input().split(' '))) # powers
Ps.reverse()
dp = N*[1]

for i in range(N):
    for j in range(i):
        if Ps[i] > Ps[j]: dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
