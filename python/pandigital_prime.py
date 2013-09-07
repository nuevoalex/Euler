import itertools
import math

primes = {}
nonPrimes = {}
def is_prime(number):
    if number in primes:
        return True
    if number in nonPrimes:
        return False
    if number % 2 == 0:
      nonPrimes[number] = True
      return False
    for divisor in xrange(3, int(math.sqrt(number))+1, 2):
        if number % divisor == 0:
            nonPrimes[number] = True
            return False
    primes[number] = True
    return True

result = None

for i in range(8, 3, -1):
  if result:
    break
  perms = reversed(sorted(itertools.permutations(range(1, i))))
  for perm in perms:
    num = int("".join(map(str, perm)))
    if is_prime(num):
      result = num
      break

print result
