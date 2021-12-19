import sys

input = sys.stdin.readline
Ts = [] # required times
Ps = [] # price earned

nday = int(input())
for _ in range(nday):
  t, p = map(int, input().split(' '))
  Ts += [t]
  Ps += [p]

def find_max_profit(nth: int, cumul_p: int, cd: int,
                    unclaimed_p: int) -> int:
  # reached the end of work day
  if nth == nday:
    cumul_p += int(cd == 0)*unclaimed_p
    return cumul_p
  else:
    # still finishing task
    if cd > 0:
      return find_max_profit(nth+1, cumul_p, cd-1, 
                             unclaimed_p)
    else:
      new_cumul_p = cumul_p + unclaimed_p
      unclaimed_p = Ps[nth]
      new_cd = Ts[nth]

      # two choices (do or skip)
      return max(find_max_profit(nth+1, new_cumul_p, new_cd-1,
                                 unclaimed_p),
                 find_max_profit(nth+1, new_cumul_p, cd, 0))


print(find_max_profit(0, 0, 0, 0))
