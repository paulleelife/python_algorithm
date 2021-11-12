num = int(input())
arr = sorted([int(x) for x in input().split(' ')])

cnt = 0 
answer = 0
for x in arr:
    cnt += 1
    if cnt >= x:
      answer += 1
      cnt = 0

print(answer) 

