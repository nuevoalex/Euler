tri_nums = [0 for i in xrange(100000)]

last = 1

for i in range(2, 100):
  tri_nums[last] = 1
  last += i

def to_num(word):
  return sum([ord(c) - 64 for c in word])

total = 0

with open("words.txt") as fd:
  for word in fd.read().split(","):
    if tri_nums[to_num(word[1:-1])]:
      print word
      total += 1

print total
