import os
import sys

class TraverseDirectory(object):
  dpath = ""
  files = []

  def __init__(self, path):
    self.dpath = path
    self.scandir(path)

  def scandir(self, path):
    if not os.path.isdir():
      return

    for f in os.listdir(path):
      if f.startswith("."):
        continue
      
      if os.path.isfile(path + "/" + f):
        self.files.append(f)
      elif os.path.isdir(path + "/" + f):
        self.scandir(path + "/" + f)


if __name__ == "__main__":
  if os.path.isdir(sys.argv[1]):
    td = TraverseDirectory(sys.argv[1])
