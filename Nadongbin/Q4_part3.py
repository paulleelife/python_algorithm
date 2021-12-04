import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

tgt = 1

for x in data:
	if x > tgt:
		break
	tgt += x 

print(tgt)
