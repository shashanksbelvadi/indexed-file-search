import os
import sys

class Driver(object):
  def __init__(self, path):
    td = TraverseDirectory(dpath)
    for f in td.files:
      ReadFile(f)

if __name__ == "__main__":
  try:
    dpath = sys.argv[1]
    if dpath != None and os.path.isdir(dpath):
      dr = Driver(dpath)
  except Exception:
    print "No directory specified."