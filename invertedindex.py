class InvertedIndex(object):
  ind = {}

  @staticmethod
  def addword(word, filepath):
    if word not in InvertedIndex.ind:
      filepaths = []
      filepaths.append(filepath)
      InvertedIndex.ind[word] = filepaths
    else:
      InvertedIndex.ind[word].append(filepath)

  @staticmethod
  def searchword(word):
    if word not in InvertedIndex.ind:
      return []
    else:
      return InvertedIndex.ind[w]
      