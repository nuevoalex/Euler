from sets import Set
import random
import collections

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[93m'
BIGRED = '\033[91m'
ENDC = '\033[0m'

class Node:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.traversable = random.choice([True, True, False])
    self.start = False
    self.end = False
    self.clear()

  def clear(self):
    self.visited = False
    self.in_path = False

  def __str__(self):
    if self.start and self.end:
      return BIGRED + "?" + ENDC
    elif self.start:
      return GREEN + "S" + ENDC
    elif self.end:
      return BLUE + "E" + ENDC
    elif self.in_path:
      return RED + "0" + ENDC
    elif self.visited and self.traversable:
      return BIGRED + "0" + ENDC
    elif self.traversable:
      return "0"
    else:
      return "X"

class Graph:

  def __init__(self, n):
    self.size = n
    self.graph = [[Node(x, y) for y in xrange(n)] for x in xrange(n)]
    start = (random.randint(0, n-1), random.randint(0, n-1))
    end = (random.randint(0, n-1), random.randint(0, n-1))
    self.start = self.graph[start[0]][start[1]]
    self.end = self.graph[end[0]][end[1]]
    self.start.start = True
    self.start.traversable = True
    self.end.end = True
    self.end.traversable = True

  def clear(self):
    for row in self.graph:
      for node in row:
        node.clear()

  def get_neighbors(self, node, traversable=True):
    neighbors = []
    if node.y != 0: # TOP
      top = self.graph[node.x][node.y-1]
      if not traversable or top.traversable:
        neighbors.append(top)
    if node.y < self.size-1: # BOTTOM
      bottom = self.graph[node.x][node.y+1]
      if not traversable or bottom.traversable:
        neighbors.append(bottom)
    if node.x != 0: # LEFT
      left = self.graph[node.x-1][node.y]
      if not traversable or left.traversable:
        neighbors.append(left)
    if node.x < self.size-1: # RIGHT
      right = self.graph[node.x+1][node.y]
      if not traversable or right.traversable:
        neighbors.append(right)
    return neighbors

  def bfs(self):
    queue = collections.deque()
    queue.append(self.start)
    while queue:
      node = queue.popleft()
      node.visited = True
      if not node.traversable:
        continue
      if node.end:
        break
      for neighbor in self.get_neighbors(node):
        if neighbor.end:
          queue.clear()
          break
        if not neighbor.visited:
          queue.append(neighbor)
    print "===BREADTH FIRST SEARCH===\n\n"
    print self
    self.clear()

  def dfs(self):
    stack = collections.deque()
    stack.append(self.start)
    while stack:
      node = stack.pop()
      node.visited = True
      if not node.traversable:
        continue
      if node.end:
        break
      for neighbor in self.get_neighbors(node):
        if neighbor.end:
          stack.clear()
          break
        if not neighbor.visited:
          stack.append(neighbor)
    print "===DEPTH FIRST SEARCH===\n\n"
    print self
    self.clear()

  def h_value(self, start, end):
    return (abs(start.x - end.x) + abs(start.y - end.y)) * 4

  def a_star(self):
    print "===A* PATHFINDING SEARCH===\n\n"
    closed_set = []
    open_set = [self.start]
    came_from = {}
    g_scores = {self.start: 0}
    f_scores = {self.start: 0 + self.h_value(self.start, self.end)}
    path_found = False
    while open_set:
      current = open_set[0]
      for node in open_set:
        if f_scores[node] < f_scores[current]:
          current = node
      current.visited = True
      if current == self.end:
        path_found = True
        break
      open_set.remove(current)
      closed_set.append(current)
      for neighbor in self.get_neighbors(current, traversable=True):
        temp_g_score = g_scores[current] + 1
        if neighbor in closed_set and temp_g_score >= g_scores[neighbor]:
          continue
        if neighbor not in closed_set or temp_g_score < g_scores[neighbor]:
          came_from[neighbor] = current
          g_scores[neighbor] = temp_g_score
          f_scores[neighbor] = temp_g_score + self.h_value(neighbor, self.end)
          if neighbor not in open_set:
            open_set.append(neighbor)

    if path_found:
      backtrace_node = self.end
      while backtrace_node != self.start:
        backtrace_node.in_path = True
        backtrace_node = came_from[backtrace_node]
    print self
    self.clear()

  def __str__(self):
    rep = ""
    for row in self.graph:
      rep += " ".join(map(str, row)) + "\n"
    return rep

if __name__ == "__main__":
  graph = Graph(10)
  print graph
  graph.dfs()
  graph.bfs()
  graph.a_star()
