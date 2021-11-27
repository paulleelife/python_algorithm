import sys
input = sys.stdin.readline

n_rise = 0 
n_fall = 0 

S = input()

for i in range(len(S)-1):
  if S[i:i+2] == '01':
    n_rise += 1
  elif S[i:i+2] == '10':
    n_fall += 1


print(min([n_rise+int(S[0]=='1'),
            n_fall+int(S[0]=='0')]))
