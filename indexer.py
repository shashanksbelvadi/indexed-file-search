import os

class Indexer(object):
  
  def __init__(self, p):
    self.ind = {}
    self.addwords(p)

  '''
    inputs:
      p: instance of Parser
    output:
      words inserted into the inverted index
  '''
  def addwords(self, p):
    for word in p.words:
      if word not in self.ind:
        paths = []
        paths.append(p.sourcepath)
        self.ind[word] = paths
      else:
        self.ind[word].append(p.sourcepath)

