import os
import sys

class TraverseDirectory(object):
  dpath = ""
  files = []

  def __init__(self):
    self.dpath = path
    self.scandir()

  def scandir(self):
    for f in os.listdir(path):
      # Hidden or OS file
      if f.startswith("."):
        continue

      if os.path.isfile(path + "/" + f):
        # File
        self.files.append(f)
      elif os.path.isdir(path + "/" + f):
        # Directory
        self.scandir(path + "/" + f)


if __name__ == "__main__":
  if os.path.isdir(sys.argv[1]):
    td = TraverseDirectory(sys.argv[1])
