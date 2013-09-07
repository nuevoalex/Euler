import math
import sys

val = int(sys.argv[1])

def seive(n):
  prime = [1 for i in range(n)]
  prime[0] = 0
  prime[1] = 0
  m = int(math.ceil(math.sqrt(n)))
  for i in range(2, m):
    if prime[i]:
      for j in range(2*i, n, i):
        prime[j] = 0
  print prime

seive(val)
