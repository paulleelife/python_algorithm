import sys

input = sys.stdin.readline

N = int(input())
home_poses = list(map(int, input().split(' ')))
home_poses.sort()
print(home_poses[(N-1)//2])
