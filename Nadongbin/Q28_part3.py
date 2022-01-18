import sys


def main():
  input = sys.stdin.readline
  N = int(input())
  sorted_list = list(map(int, input().split(' ')))

  lower_idx = 0
  if sorted_list[lower_idx] == lower_idx: 
    print(lower_idx)
    return
  upper_idx = len(sorted_list) - 1
  if sorted_list[upper_idx] == upper_idx:
    print(upper_idx)
    return

  while True:
    curr_idx = (upper_idx+lower_idx)//2
    if sorted_list[curr_idx] > curr_idx:
      upper_idx = curr_idx
    elif sorted_list[curr_idx] < curr_idx:
      lower_idx = curr_idx
    elif sorted_list[curr_idx] == curr_idx:
      print(curr_idx)
      return
    if (upper_idx - lower_idx) <= 1:
      print(-1)
      return


if __name__ == "__main__":
  main()
