import time
import itertools

nums = range(1, 10)

products = {}

def without(initial, neg):
  return [num for num in initial if num not in neg]

total = 0

start = time.time()
for (a, b, c, d, e) in itertools.permutations(nums, 5):
  product = ((a * 10) + b) * ((c * 100) + (d * 10) + e)
  if product in products:
    continue
  if sorted(map(int, str(product)) + [a, b, c ,d, e]) == nums:
    products[product] = True
    print "%s * %s = %d" % (a*10+b, c*100+d*10+e, product)
    total += product
    continue
  product = a * ((b * 1000) + (c * 100) + (d * 10) + e)
  if product in products:
    continue
  if sorted(map(int, str(product)) + [a, b, c ,d, e]) == nums:
    products[product] = True
    print "%s * %s = %d" % (a, b*1000+c*100+d*10+e, product)
    total += product


print total
print '\n','Executed in',time.time()-start,'sec'
