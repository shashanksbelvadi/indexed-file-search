class Indexer(object):
  
  def __init__(self):
    self.ind = {}

  '''
    inputs:
      p: instance of Parser.
    output:
      words inserted into the inverted index.
  '''
  def addwords(self, p):
    for word in p.words:
      self.ind[word] = self.ind.get(word, [])
      self.ind[word].append(p.sourcepath)

  def getlocations(self, qwords):
    locations = []
    for q in qwords:
      locations.extend(self.ind.get(q, []))
    return locations

  @staticmethod
  def printlocations(locations):
    for l in locations:
      print l
