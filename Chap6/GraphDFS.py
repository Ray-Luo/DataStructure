def graphDFS(G, start, goal):
  V, E = G
  stack = Stack()
  visited = Set()
  stack.push(start)

  while not stack.isEmpty():
    current = stack.pop()
    visited.add(current)

  if current == goal:
    return True

  for v in adjacent(current, E):
    if not v in visited:
      stack.push(v)

  return False


    
