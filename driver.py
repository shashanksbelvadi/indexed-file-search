import os
import sys
import traverser
import parser
import indexer

class Driver(object):

  def __init__(self, path, searchword):
    i = indexer.Indexer()
    t = traverser.Traverser(dpath)
    for f in t.files:
      i.addwords(parser.Parser(f))
    i.printlocations(i.getlocations(searchword))

if __name__ == "__main__":
  try:
    dpath = sys.argv[1]
    searchword = sys.argv[2]
    if dpath != None and os.path.isdir(dpath):
      dr = Driver(dpath, searchword)
  except Exception:
    raise
