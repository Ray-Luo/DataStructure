class BinarySearchTree:

  class __Node:
    def __init__(self, val, left = None, right = None):
      self.val = val
      self.left = left
      self.right = right

    def getVal(self):
      return self.val

    def setVal(self, newVal):
      self.val = newVal

    def getLeft(self):
      return self.left

    def getRight(self):
      return self.right

    def setLeft(self, newLeft):
      self.left = newLeft

    def setRight(self, newRight):
      self.right = newRight

    def __iter__(self):
      if self.left != None:
        for elem in self.left:
          yield elem

      yield self.val

      if self.right != None:
        for elem in self.right:
          yield elem


  def __init__(self):
    self.root = None


  def insert(self, val):  
    
    def __insert(root, val):
      if root == None:
        return BinarySearchTree.__Node(val)

      if val < root.getVal():
        root.setLeft(__insert(root.getLeft(), val))
      else:
        root.setRight(__insert(root.getRight(), val))

      return root

    self.root = __insert(self.root, val)


  def __iter__(self):
    if self.root != None:
      return self.root.__iter__()
    else:
      return [].__iter__()

def main():
  s = input("Enter a list of numbers: ")
  lst = s.split()

  tree = BinarySearchTree()

  for x in lst:
    tree.insert(float(x))

  for x in tree:
    print(x)

if __name__ == "__main__":
  main()




































