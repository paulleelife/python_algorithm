import sys

input = sys.stdin.readline

def main():
  N, tgt_val = map(int, input().split(' '))
  vals = list(map(int, input().split(' ')))

  lower_tgt_idx = None
  upper_tgt_idx = None

  lower_idx = 0
  upper_idx = len(vals) - 1

  # boundary condition
  if vals[lower_idx] == tgt_val: lower_tgt_idx = lower_idx
  if vals[lower_idx] > tgt_val:
    print(-1)
    return

  if vals[upper_idx] == tgt_val: upper_tgt_idx = upper_idx
  if vals[upper_idx] < tgt_val:
    print(-1)
    return

  curr_lower_idx = lower_idx
  curr_upper_idx = upper_idx

  # first find upper_tgt_idx
  while True:
    curr_idx = (curr_upper_idx+curr_lower_idx)//2
    if upper_tgt_idx is not None:
      if upper_idx - upper_tgt_idx <= 1: break
    if vals[curr_idx] == tgt_val:
      curr_lower_idx = curr_idx
      upper_tgt_idx = curr_idx
    elif vals[curr_idx] < tgt_val:
      curr_lower_idx = curr_idx
      lower_idx = curr_idx
    elif vals[curr_idx] > tgt_val:
      curr_upper_idx = curr_idx
      upper_idx = curr_idx
    # no tgt val found
    if (curr_upper_idx-curr_lower_idx) <= 1 and upper_tgt_idx is None:
      print(-1) 
      return

  # then find lower_tgt_idx
  curr_lower_idx = lower_idx
  curr_upper_idx = upper_tgt_idx

  while True:
    curr_idx = (curr_upper_idx+curr_lower_idx)//2
    if lower_tgt_idx is not None:
      if lower_tgt_idx - lower_idx <= 1: break
    if vals[curr_idx] == tgt_val:
      curr_upper_idx = curr_idx
      lower_tgt_idx = curr_idx
    elif vals[curr_idx] < tgt_val:
      curr_lower_idx = curr_idx
      lower_idx = curr_idx
    elif vals[curr_idx] > tgt_val:
      curr_upper_idx = curr_idx
      upper_idx = curr_idx
    
  # count the number of target vlaues
  print(upper_tgt_idx-lower_tgt_idx+1)

if __name__ == "__main__":
  main()
