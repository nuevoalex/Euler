def is_palindromic(word):
  return word == "".join(reversed(word))

def is_palindromic_pair(num):
  bin_num = bin(num)[2:]
  str_num = str(num)
  if str_num[-1] == "0" or bin_num[-1] == "0":
    return False
  return is_palindromic(str(num)) and is_palindromic(bin_num)

print sum([num for num in xrange(1000000) if is_palindromic_pair(num)])
