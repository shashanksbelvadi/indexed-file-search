import os

class Traverser(object):
  
  def __init__(self, dirpath):
    self.files = []
    self.getfilelist(dirpath)

  def getfilelist(self, dirpath):
    for (dpath, subdirs, filelist) in os.walk(dirpath):
      for flist in filelist:
        temp = [os.path.join(dirpath, f) for f in filelist if not self.is_hidden_file(f)]
        self.files.extend(temp)

  @staticmethod
  def is_hidden_file(f):
    return f.startswith(".")
