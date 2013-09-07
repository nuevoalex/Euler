def divide(a, b):
  sign = -1 if (a < 0 and b > 0) or (a >= 0 and b < 0) else 1
  a, b = abs(a), abs(b)
  if b == 0:
    raise ValueError("Not cool man")
  result = 0
  while a >= b:
    result += sign
    a -= b
  return result

print divide(4, 2)
print divide(40, 2)
print divide(0, 1)
print divide(-1, 2)
print divide(3, -2)
print divide(10, 7)
print divide(7, 2)
