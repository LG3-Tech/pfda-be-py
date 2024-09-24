import os
import shutil

def saveFiles(files, filesFolder):
  uploads_dir = os.path.join(filesFolder)
  os.makedirs(uploads_dir, exist_ok=True)

  for emphasisFile in files:
    name = emphasisFile['name']
    file = emphasisFile['file']
    file_extension = file.filename.split(".")[1]

    filename = [name, file_extension]

    file.save(os.path.join(uploads_dir, ".".join(filename)))


def removeFiles(filesFolder):
  uploads_dir = os.path.join(filesFolder)
  shutil.rmtree(uploads_dir)
