import sys
import numpy as np

input = sys.stdin.readline
n_case = int(input())

for _ in range(n_case):
  n, m = map(int, input().split(' '))
  gold_arr = np.array(list(map(int, input().split(' '))), dtype=int)

  viterbi_box = np.zeros([n, m], dtype=int)
  
  # initialize viterbi box
  for col in range(m):
    for row in range(n):
      viterbi_box[row, col] = gold_arr[m*row+col]
   
  # start viterbi algorithm
  for col in range(1, m):
    for row in range(n):
      viterbi_box[row, col] += np.max(viterbi_box[np.clip(np.array([row-1, row, row+1]), 0, n-1), col-1])

  # give the max value of the last column
  print(np.max(viterbi_box[:, -1]))
