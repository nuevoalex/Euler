import operator

digits = ""

for i in range(500000):
  digits += str(i)

print reduce(operator.mul, [int(digits[n]) for n in [pow(10, i) for i in range(7)]])
