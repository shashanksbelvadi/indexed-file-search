import os

class Parser(object):
  
  def __init__(self, source):
    try:
      self.sourcepath = os.path.abspath(source)
      handle = open(source, "r")
      self.words = self.parse(handle)
      handle.close()
    except IOError:
      print "Couldn't read file."
    except Exception:
      print "Bad input."
      raise

  @staticmethod
  def parse(handle):
    words = []
    for line in handle:
      line = line.rstrip().split(" ")
      for w in line:
        if w not in words:
          words.append(w)
    return words
