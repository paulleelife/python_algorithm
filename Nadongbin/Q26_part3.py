import sys
import heapq

input = sys.stdin.readline
N = int(input())

h = []
total_sum = 0

for i in range(N):
    heapq.heappush(h, int(input()))

while len(h) > 1:
    one = heapq.heappop(h)
    two = heapq.heappop(h)
    curr_sum = one + two
    total_sum += curr_sum
    heapq.heappush(h, curr_sum)

print(total_sum)
        
