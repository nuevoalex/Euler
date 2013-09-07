last = 0
num = 1

if __name__ == "__main__":
  i = 1
  while len(str(num)) < 1000:
    i+=1
    num, last = num + last, num
  print i
