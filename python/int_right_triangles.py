def get_sides(p):
  sides = [p]
  for n in range(p/3, p/2):
    for i in range(1, (p-n)/2):
      j = p - n - i
      if pow(i, 2) + pow(j, 2) == pow(n, 2):
        sides += [(i, j, n)]
  return sides

max_item = []

for i in range(1000):
  sides = get_sides(i)
  if len(sides) > len(max_item):
    max_item = sides

print max_item
