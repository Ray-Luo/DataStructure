class PyList:
  
  def __init__(self, contents=[], size=10):
    self.items = [None] * size
    self.numItems = 0
    self.size = size

    for e in contents:
      self.append(e)


  def __getitem__(self, index):
    if index >= 0 and index < self.numItems:
      return self.items[index]
    raise IndexError("PyList index out of range")

  def __setitem__(self, index, val):
    if index >=0 and index < self.numItems:
      self.items[index] = val
      return
    
    raise IndexError("PyList index out of range")

  def __add__(self, other):
    result = PyList(size=self.numItems + other.numItems)

    for i in range(self.numItems):
      result.append(self.items[i])

    for i in range(self.numItems):
      result.append(other.items[i])

    return result

  def __makeroom(self):
    newlen = (self.size // 4) + self.size + 1
    newlst = [None] * newlen
    for i in range(self.numItems):
      newlst[i] = self.items[i]

    self.items = newlst
    self.size = newlen


  def append(self, item):
    if self.numItems == self.size:
      self.__makeroom()

    self.items[self.numItems] = item
    self.numItems += 1

  def insert(self,i,e):
    if self.numItems == self.size:
      self.__makeroom()
    
    if i < self.numItems:
      for j in range(self.numItems-1,i-1,-1):
        self.items[j+1] = self.items[j]

      self.items[i] = e
      self.numItems += 1

    else:
      self.append(e)


  def __delitem__(self, index):
    for i in range(index, self.numItems-1):
      self.items[i] = self.items[i+1]
    self.numItems -= 1


  def __eq__(self, other):
    if type(other) != type(self):
      return False

    if self.numItems != other.numItems:
      return False

    for i in range(self.numItems):
      if self.items[i] != other.items[i]:
        return False

    return True

  def __iter__(self):
    for i in range(self.numItems):
      yeild self.items[i]

  def __len__(self):
    return self.numItems

  def __contains__(self,item):
    for i in range(self.numItems):
      if self.items[i] == item:
        return True
    return False

  def __str__(self):
    s = "["
    for i in range(self.numItems):
      s = s + repr(self.items[i])
      if i < self.numItems - 1:
        s = s + ", "
    s = s + "]"
    return s

  def __repr__(self):
    s = "PyList(["
    for i in range(self.numItems):
      s = s + repr(self.items[i])
      if i < self.numItems - 1:
        s = s + ", "

    s = s + "])"
    return s

  def select(seq, start):
    minIndex = start
  
    for j in range(start+1, len(seq)):
      if seq[minIndex] > seq[j]:
        minIndex = j
    
    return minIndex

  def selSort(seq):
    for i in range(len(seq)-1):
      minIndex = select(seq,i)
      tmp = seq[i]
      seq[i] = seq[minIndex]
      seq[minIndex] = tmp


  def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    while i < mid and j < stop:
      if seq[i] < seq[j]:
        lst.append(seq[i])
        i+=1
      else：
        lst.append(seq[j])
        j+=1

    while i < mid:
      lst.append(seq[i])
      i+=1

    for i in range(len(lst)):
      seq[start+i] = lst[i]

  
  def mergeSortRecursively(seq, start, stop):
    if start >= stop-1:
      return
  
    mid = (start + stop) // 2

    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

  def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))


  def partition(seq, low, high):
    i = low-1
    pivot = seq[high]
    
    for j in range(low, high):
      if seq[j] <= pivot:
        i = i + 1
        seq[i], seq[j] = seq[j], seq[i]
    
    seq[i+1], seq[high] = seq[high], seq[i+1]
    return (i+1)

  def quickSort(seq,low,high):
    if low < high:
      pivot = partition(seq, low, high)
      quickSort(seq, low, pivot-1)
      quickSort(seq, pivot+1, high)






















  





















