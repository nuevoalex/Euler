largest = 0

def is_pandigital(str_num):
  return len(str_num) == 9 and all([c in str_num for c in "123456789"])

for n in range(2, 6):
  mults = range(1,n+1)
  for num in range(1, pow(10, 6-n)):
    product = "".join([str(num * mult) for mult in mults])
    if int(product) > largest and is_pandigital(product):
      largest = int(product)

print largest
