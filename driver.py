import os
import sys
import traverser
import parser
import indexer

class Driver(object):

  '''
    inputs:
      path        -----> absoulute path of directory.
      searchwords -----> list of query words.
  '''
  def __init__(self, path, searchwords):
    i = indexer.Indexer()
    t = traverser.Traverser(dpath)
    for f in t.files:
      i.addwords(parser.Parser(f))
    i.printlocations(i.getlocations(searchwords))

if __name__ == "__main__":
  try:
    dpath = sys.argv[1]
    searchwords = sys.argv[2:]
    if dpath != None and os.path.isdir(dpath):
      dr = Driver(dpath, searchwords)
  except Exception:
    raise
