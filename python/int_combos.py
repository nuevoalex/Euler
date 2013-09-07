import math

def num_distinct_terms(lim):
  found = set()
  for a in xrange(2, lim + 1):
    for b in xrange(2, lim + 1):
      found.add(math.pow(a, b))
  print len(found)

num_distinct_terms(100)
