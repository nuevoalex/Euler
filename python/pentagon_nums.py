import itertools

pentagons = []
is_pentagon = [0 for i in xrange(20000000)]

last = 1
add = 4

for i in xrange(2500):
  pentagons.append(last)
  is_pentagon[last] = 1
  last += add
  add += 3

lowest = None

for j, k, in itertools.combinations(pentagons, 2):
  if is_pentagon[j+k]:
    diff = abs(j-k)
    if is_pentagon[diff]:
      print (j,k)
      if not lowest or diff < lowest:
        lowest = diff

print lowest
