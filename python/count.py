def count(n):
   print sum([1 for i in xrange(n) if '4' not in str(i)])

count(20)
