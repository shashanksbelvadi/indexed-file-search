class Indexer(object):
  
  def __init__(self):
    self.ind = {}

  '''
    inputs:
      p: instance of Parser
    output:
      words inserted into the inverted index
  '''
  def addwords(self, p):
    for word in p.words:
      if word not in self.ind:
        self.ind[word] = [p.sourcepath]
      else:
        self.ind[word].append(p.sourcepath)

