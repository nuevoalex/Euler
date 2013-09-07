class Thing(object):

  def __init__(self):
    self._val = None
    self.bit = 0

  @property
  def val(self):
    return self._val

  @val.setter
  def val(self, value):
    self.bit = 1
    self._val = value

if __name__ == "__main__":
  test = Thing()
  test.val = "value"
  print test.val
  print test.bit
