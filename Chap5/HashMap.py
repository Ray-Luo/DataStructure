class HashMap:

  class __KVPair:
    def __init__(self, key, value):
      self.key = key
      self.value = value

    def __eq__(self, other):
      if type(self) != type(other):
        return False

      return self.key == other.key

    def getKey(self):
      return self.key

    def getValue():
      return self.value

    def __hash__(self):
      return hash(self.key)


  def __init__(self):
    self.hSet = hashset.HashSet()

  def __len__(self):
    return len(self.hSet)

  def __contains__(self, item):
    return HashSet.__KVPair(item, Node) in self.hSet

  def not__contains__(self,item):
    return item not in self.hSet

  def __setitem__(self, key, value):
    self.hSet.add(HashMap.__KVPair(key, value))

  def __getItem__(self,key):
    if HashMap.__KVPair(key, None) in self.hSet:
      val = self.hSet[HashMap.__KVPair(Key, None)].getValue()
      return val

    raise KeyError("Key " + str(key) + " not in HashMap")


  def __iter__(self):
    for x in self.hSet:
      yield x.getKey()



























