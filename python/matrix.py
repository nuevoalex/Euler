import random

class Matrix(object):

  def __init__(self, w, h, populate=True):
    self.w = w
    self.h = h
    if populate:
      self.matrix = [[random.randint(0, 9) for j in xrange(w)] for i in xrange(h)]
    else:
      self.matrix = [[0 for j in xrange(w)] for i in xrange(h)]

  def __add__(self, other):
    if self.w != other.w or self.h != other.h:
      return "Not compatible for addition"
    result = Matrix(self.w, self.h, False)
    for h in range(self.h):
      for w in range(self.w):
        result.matrix[h][w] = self.matrix[h][w] + other.matrix[h][w]
    return result

  def __sub__(self, other):
    if self.w != other.w or self.h != other.h:
      return "Not compatible for subtraction"
    result = Matrix(self.w, self.h, False)
    for h in range(self.h):
      for w in range(self.w):
        result.matrix[h][w] = self.matrix[h][w] - other.matrix[h][w]
    return result

  def __mul__(self, other):
    if self.h != other.w:
      return "Not compatible for multiplication"
    result = Matrix(other.w, self.h, False)
    for h in range(self.h):
      for w in range(other.w):
        result.matrix[h][w] = sum([i*j for i, j in zip(self.matrix[h], [row[w] for row in other.matrix])])
    return result

  def __str__(self):
    rep = ""
    for row in self.matrix:
      rep += " ".join(map(str, row)) + "\n"
    return rep

if __name__ == "__main__":
  x, y, z = [random.randint(1,4) for i in range(3)]
  matrix1 = Matrix(x, y)
  matrix2 = Matrix(y, z)
  print matrix1
  print matrix2
  print "matrix1 + matrix2:\n%s" % (matrix1 + matrix2)
  print "matrix1 - matrix2:\n%s" % (matrix1 - matrix2)
  print "matrix1 * matrix2:\n%s" % (matrix1 * matrix2)
