class KeyValue(object):

  def __init__(self, key, value):
    self.key = key
    self.value = value


class HashTable(object):

  SIZE = 10000

  def __init__(self):
    self.values = []
    self.key_values = [[] for i in range(self.SIZE)]

  def __setitem__(self, key, value):
    hash_key = hash(key) % self.SIZE
    bucket = self.key_values[hash_key]
    for item in bucket:
      if key == item.key:
        item.value = value
        return key
    bucket.append(KeyValue(key, value))

  def __delitem__(self, key):
    hash_key = hash(key) % self.SIZE
    bucket = self.key_values[hash_key]
    for item in bucket:
      if key == item.key:
        bucket.remove(item)
        return key
    raise KeyError("%s not found in Hash" % key)

  def __getitem__(self, key):
    hash_key = hash(key) % self.SIZE
    bucket = self.key_values[hash_key]
    for item in bucket:
      if key == item.key:
        return item.value
    return None

  def __str__(self):
    val = ""
    for bucket in self.key_values:
      for item in bucket:
        val += "%s: %s\n" % (item.key, item.value)
    return val

if __name__ == "__main__":
  test = HashTable()
  test["2"] = "String two"
  test[2] = "Digit two"
  test[1] = "NOPE"
  del test[1]
  test[(2,)] = "Tuple two"
  print test

