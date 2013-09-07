example = list(reversed(sorted([2,7,4,2,9,11,9,4,2,23,4,6,12])))
print example
d = 25

if __name__ == "__main__":
  j = 0
  for i in range(len(example)):
    print 'huh'
    while j < len(example) and (example[i]-example[j] > d):
      print 'whut'
      j += 1
    if (example[i] - example[j] == d):
      print 'yes'
  print j
