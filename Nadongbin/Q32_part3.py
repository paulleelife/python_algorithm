import sys

input = sys.stdin.readline
n = int(input())

pyramids = []

# initialize pyramids
for i in range(n):
    pyramids += [list(map(int, input().split(' ')))]

for row in range(1, n):
  for col in range(row+1):
    # left edge
    if col == 0: pyramids[row][col] += pyramids[row-1][col]
    # right edge
    elif col == row: pyramids[row][col] += pyramids[row-1][col-1]
    else: pyramids[row][col] += max(pyramids[row-1][col], 
                                    pyramids[row-1][col-1])

print(max(pyramids[-1]))
