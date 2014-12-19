import os
import sys
import traverser
import parser
import indexer

class Driver(object):
  def __init__(self, path):
    i = indexer.Indexer()
    t = traverser.Traverser(dpath)
    for f in t.files:
      i.addwords(parser.Parser(f))
    print i.ind

if __name__ == "__main__":
  try:
    dpath = sys.argv[1]
    if dpath != None and os.path.isdir(dpath):
      dr = Driver(dpath)
  except Exception:
    print "No directory specified."
    raise