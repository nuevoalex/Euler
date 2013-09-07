import math

def is_prime(n):
  n = abs(n)
  for i in xrange(2, int(math.ceil(math.sqrt(n)))):
    if n % i == 0:
      return False
  return True


def quad_n(a, b):
  i = 0
  while True:
    n = pow(i, 2) + (a * i) + b
    if not is_prime(n):
      break
    i += 1
  return i - 1


if __name__ == "__main__":
  n = 1000
  biggest_quad_n = 0
  cur_prod = None
  for i in xrange(-n, n):
    for j in xrange(-n, n):
      qn = quad_n(i, j)
      if qn > biggest_quad_n:
        biggest_quad_n = qn
        cur_prod = i * j
  print cur_prod
