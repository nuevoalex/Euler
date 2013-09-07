import sys

def base_conv(num, base=2):
  converted = ""
  while num:
    num, mod = divmod(num, base)
    converted = str(mod) + converted
  return converted

if __name__ == "__main__":
  print base_conv(int(sys.argv[1]), int(sys.argv[2]))
