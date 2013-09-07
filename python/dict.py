class KeyValue:

  def __init__(self, key, value):
    self.key = key
    self.value = value


class HashTable:

  SIZE = 10000

  def __init__(self):
    self.values = [[] for i in range(self.SIZE)]
    self.map_cache = []

  def hashify(self, item):
    return hash(item) % self.SIZE

  def resize(self):
    pass

  def __setitem__(self, key, value):
    hash_key = self.hashify(key)
    bucket = self.values[hash_key]
    for item in bucket:
      if item.key == key:
        item.value = value
        return item
    self.map_cache.append(key)
    bucket.append(KeyValue(key, value))

  def __getitem__(self, key):
    hash_key = self.hashify(key)
    bucket = self.values[hash_key]
    for item in bucket:
      if item.key == key:
        return item.value
    return None # Could also raise KeyError (this is what python dicts do for example)

  def __delitem__(self, key):
    hash_key = self.hashify(key)
    bucket = self.values[hash_key]
    for item in bucket:
      if item.key == key:
        bucket.remove(item)
    self.map_cache.remove(key)
    return None # Could also raise KeyError (this is what python dicts do for example)

  def __str__(self):
    _str = ""
    for key in self.map_cache:
      bucket = self.values[self.hashify(key)]
      for item in bucket:
        _str += "%s: %s\n" % (item.key, item.value)
    return _str

if __name__ == "__main__":
  test = HashTable()
  test[2] = "two"
  test[2.5] = "two point 5"
  test["2"] = 2
  test["2.5"] = 2.5
  test[(2,5)] = "tuples!"
  del test["2"]
  test[2] = "NEW TWO"
  print test
