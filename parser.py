import os
import string

class Parser(object):
  
  def __init__(self, source):
    try:
      self.sourcepath = os.path.abspath(source)
      with open(self.sourcepath) as handle:
        self.words = self.parse(handle)
    except IOError:
      print "Couldn't read file."
    except Exception:
      raise

  @staticmethod
  def parse(handle):
    words = []
    for line in handle:
      line = line.rstrip().split(" ")
      for w in line:
        w = Parser.removepunctuation(w)
        if w not in words:
          words.append(w)
    return words

  @staticmethod
  def removepunctuation(word):
    '''
      Note:
        string.maketrans() -----> creates translation table.
        string.punctuation -----> list of punctuation symbols.
    '''
    return word.translate(string.maketrans("", ""), string.punctuation)
