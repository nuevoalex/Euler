import random

def merge(a, b):
  result = []
  while a and b:
    if a[0] < b[0]:
      result.append(a.pop(0))
    else:
      result.append(b.pop(0))
  result += a
  result += b
  return result

def merge_sort(stuff):
  if len(stuff) < 2:
    return stuff
  pivot = len(stuff)/2
  left, right = stuff[:pivot], stuff[pivot:]
  return merge(merge_sort(left), merge_sort(right))

def quick_sort(stuff):
  if len(stuff) < 2:
    return stuff
  pivot = stuff.pop(len(stuff)/2)
  left, right = [], []
  for item in stuff:
    if item < pivot:
      left.append(item)
    else:
      right.append(item)
  return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
  sample = [random.randint(0,99) for i in xrange(20)]
  print sample
  print merge_sort(sample)
  print quick_sort(sample)
