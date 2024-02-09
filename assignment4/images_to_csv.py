import csv
import numpy as np
import os
import sys
from PIL import Image, UnidentifiedImageError

assert len(sys.argv) == 2
currDir = f"rps-data/rps-{sys.argv[1]}-set"
csvFileName = f"rps-{sys.argv[1]}-data.csv"

def createFileList(myDir, format='.png'):
  fileList = []
  print(f"Creating file list for {myDir}.")
  labels = []
  names = []
  keywords = {"paper": "1","rock": "2","scissors":"3"} # keys and values to be changed as needed
  for root, dirs, files in os.walk(myDir, topdown=True):
    for name in sorted(files):
      if name.endswith(format):
        fullName = os.path.join(root, name)
        fileList.append(fullName)
      for keyword in keywords:
        if keyword in name:
          labels.append(keywords[keyword])
        else:
          continue
      names.append(name)
  return fileList, labels, names

# load the original image
myFileList, labels, names = createFileList(currDir)
i = 0

for index, file in enumerate(myFileList):
  try:
    img_file = Image.open(file)

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=int).reshape((width, height))
    value = value.flatten()
    value = np.append(value,labels[i])
    i +=1
    with open(csvFileName, 'a') as f:
      writer = csv.writer(f)
      writer.writerow(value)
  except UnidentifiedImageError:
    print(f"Failed to convert {file}.")