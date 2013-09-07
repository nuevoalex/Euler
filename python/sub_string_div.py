import itertools

primes = [2,3,5,7,11,13,17]

def prime_subs(num_str):
  num_str = "".join(num_str)
  for i in range(1,8):
    num = int(num_str[i:i+3])
    if num % primes[i-1] != 0:
      return False
  print num_str
  return True

print sum((int("".join(perm)) for perm in itertools.permutations("0123456789")
  if prime_subs(perm)))
