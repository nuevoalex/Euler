import math

def seive(n):
  primes = [1 for num in xrange(n)]
  primes[0] = 0
  primes[1] = 0
  for m in xrange(2, int(math.sqrt(n))):
    if primes[m]:
      for n in range(2 * m, n, m):
        primes[n] = 0
  return primes

def get_truncs(word):
  truncs = [word]
  for i in range(1, len(word)):
    truncs += [word[i:], word[:-i]]
  return truncs

def is_trunc_prime(num):
  str_num = str(num)
  return all([primes[int(trunc)]
    for trunc in get_truncs(str_num)
  ])

primes = seive(1000000)

total = 0
for num in xrange(11, 1000000):
  if is_trunc_prime(num):
    total += num

print total
