import os

class ReadFile(object):
  filepath = ""

  def __init__(self, filepath):
    self.filepath = filepath
    self.parsefile()

  def parsefile(self):
    try:
      for line in open(filepath):
        input_words = line.rstrip().split(" ")
        for w in input_words:
          InvertedIndex.addword(w)
    except IOError:
      print "Couldn't read file."
    except Exception:
      raise
