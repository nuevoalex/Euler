import math
import sys

def euclid(n1, n2):
  new_n = n1 % n2
  if new_n == 0:
    return n2
  else:
    return euclid(n2, new_n)
  return "fail"

if __name__ == "__main__":
  num1, num2 = int(sys.argv[1]), int(sys.argv[2])
  num1, num2 = max(num1, num2), min(num1, num2)
  print euclid(num1, num2)
