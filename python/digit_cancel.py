import fractions

nums = range(11, 99)

def is_non_trivial_curious_fraction(numerator, denominator):
  str_num, str_dem = str(numerator), str(denominator)
  if str_num[0] in str_dem:
    str_rem = str_num[0]
    new_num = int(str_num[1])
    dem_loc = 1 if str_dem.find(str_rem) == 0 else 0
    new_dem = int(str_dem[dem_loc])
  elif str_num[1] in str_dem:
    str_rem = str_num[1]
    new_num = int(str_num[0])
    dem_loc = 1 if str_dem.find(str_rem) == 0 else 0
    new_dem = int(str_dem[dem_loc])
  else:
    return False
  if not new_dem:
    return False
  return fractions.Fraction(numerator, denominator) == fractions.Fraction(new_num, new_dem)


if __name__ == "__main__":
  prod = 1
  for index, numerator in enumerate(nums):
    for denominator in nums[index+1:]:
      if not numerator % 10 and not denominator % 10:
        continue
      if is_non_trivial_curious_fraction(numerator, denominator):
        print "%d / %d" % (numerator, denominator)
        prod *= fractions.Fraction(numerator, denominator)
  print prod
