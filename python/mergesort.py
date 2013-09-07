import random

nums = [random.randint(0,20) for r in xrange(10)]
print "Staring list: %s" % nums

def merge(list1, list2):
  result = []
  i, j = 0, 0
  while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
      result.append(list1[i])
      i += 1
    else:
      result.append(list2[j])
      j += 1
  result += list1[i:]
  result += list2[j:]
  return result

def mergesort(num_list):
  if len(num_list) < 2:
    return num_list
  pivot = len(num_list)/2
  left, right = num_list[:pivot], num_list[pivot:]
  return merge(mergesort(left), mergesort(right))

if __name__== "__main__":
  print "Sorted list: %s" % mergesort(nums)
