class Vertex:

  def __init__(self, vertexId, x, y, label):
    self.vertexId = vertexId
    self.x = x
    self.y = y
    self.label = label
    self.adjacent = []
    self.previous = None


class Edge:

  def __init__(self, v1, v2, weight=0):
    self.v1 = v1
    self.v2 = v2
    self.weight = weight


  def __lt__(self, other):
    return self.weight < other.weight


