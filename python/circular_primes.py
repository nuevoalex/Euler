import sets
import math
import itertools

def seive(n):
  prime = [1 for i in range(n)]
  prime[0] = 0
  prime[1] = 0
  m = int(math.ceil(math.sqrt(n)))
  for i in range(2, m):
    if prime[i]:
      for j in range(2*i, n, i):
        prime[j] = 0
  return prime

def rotations(num):
  str_num = str(num)
  rots = [num]
  for i in range(len(str_num)-1):
    str_num = str_num[1:] + str_num[0]
    if not str_num.startswith("0"):
      rots.append(int(str_num))
  return sets.Set(rots)

prime = seive(1000000)
circulars = []

for num in range(2, 1000000):
  if num in circulars:
    continue
  rots = rotations(num)
  nope = False
  for rot in rots:
    if not prime[rot]:
      nope = True
      break
  if not nope:
    print rots
    circulars += rots

print len(circulars)
