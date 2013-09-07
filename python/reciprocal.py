import decimal
import math

decimal.getcontext().prec = 5112

def decimal_cycle_length(num):
  decs = str(decimal.Decimal(1)/decimal.Decimal(num))[2:-1]
  for i in xrange(1, int(math.ceil(len(decs)/2.0))):
    rem = decs.replace(decs[:i], "")
    if not rem or decs[:i].startswith(rem):
      return i
  return 0

if __name__ == "__main__":
  longest_val = 0
  winrar = None
  for i in xrange(2, 1000):
    dc = decimal_cycle_length(i)
    if dc:
      print "%d: %d" % (i, dc)
    if dc > longest_val:
      winrar = i
      longest_val = dc
  print winrar
