num_arr = [int(n) for n in input()]

answer = num_arr[0] # initial value
for i in range(1, len(num_arr)):
  answer = max([answer*num_arr[i], answer+num_arr[i]])

print(answer)