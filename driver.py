import os
import sys
import traverser
import parser
import indexer

class Driver(object):
  def __init__(self, path):
    t = traverser.Traverser(dpath)
    for f in t.files:
      indexer.Indexer(parser.Parser(f))

if __name__ == "__main__":
  try:
    dpath = sys.argv[1]
    if dpath != None and os.path.isdir(dpath):
      dr = Driver(dpath)
  except Exception:
    print "No directory specified."
    raise