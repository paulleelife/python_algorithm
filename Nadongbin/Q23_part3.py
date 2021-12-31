import sys

input = sys.stdin.readline

N = int(input())
infos = []

# initialize scores
for i in range(N):
  infos += [list(input().split(' '))]

infos.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
  print(infos[i][0])
