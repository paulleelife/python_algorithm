import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

ans = len(list(combinations(data, 2)))
for i in range(m):
    ans -= len(list(combinations(range(data.count(i+1)), 2)))

print(ans)
