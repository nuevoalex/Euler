import random

nums = [random.randint(0,20) for r in xrange(10)]
print "Staring list: %s" % nums

def quicksort(num_list):
  if len(num_list) < 2:
    return num_list
  pivot = num_list.pop(len(num_list)/2)
  lessers, greaters = [], []
  for i in range(len(num_list)):
    val = num_list[i]
    if val < pivot:
      lessers.append(val)
    elif val >= pivot:
      greaters.append(val)
  return quicksort(lessers) + [pivot] + quicksort(greaters)

if __name__== "__main__":
  print "Sorted list: %s" % quicksort(nums)
