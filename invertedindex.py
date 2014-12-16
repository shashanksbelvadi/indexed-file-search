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