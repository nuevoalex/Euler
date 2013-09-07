def magic_sum(n):
  nums = []
  for i in xrange(1, 1000000):
    str_num = str(i)
    cur_sum = 0
    cur_str = ""
    for j in range(len(str_num)):
      cur_str += str_num[j]
      cur_num  = int(str_num[j])
      cur_sum += pow(cur_num, n)
    if str(cur_sum) == cur_str:
      nums.append(cur_sum)
  return sum(nums)

print magic_sum(4)
