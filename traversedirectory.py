class TraverseDirectory(object):
  dpath = ""
  files = []

  def __init__(self, path):
    self.dpath = path
    self.scandir(path)

  def scandir(self, path):
    for f in os.listdir(path):
      # Hidden or OS files
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
