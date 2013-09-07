list1 = [1,2,3,4]

list2 = [4,6,7,7,7,7,8,9]

t = 12

def find_pair(l1, l2, target):
  for num1 in l1:
    for num2 in l2:
      summed = num1 + num2
      if summed < target:
        continue
      if target == num1 + num2:
         return (num1, num2)
      elif summed > target:
        break
  return (None, None)

print find_pair(list1, list2, t)
