#!/usr/bin/python
import os
import re

def readFile(fileName):
  f = open(fileName)
  txt = f.read()
  f.close()
  return txt

def writeFile(pathFile, data):
  f = open(pathFile, "w")
  f.write("\n".join(str(item) for item in data))
  f.close()

def createDir(dir):
  try: 
    os.makedirs(dir)
  except OSError:
      if not os.path.isdir(path):
          raise

#___________START INITIALIZE__________
path = "../Datasets/May"
pathMerge = "../Datasets/may.txt"
files = []

#_______MAKE FILES IN ARRAY___________
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if '.txt' in file:
      files.append(os.path.join(r, file))

query = ""
mergePairs = []
for i, f in enumerate(files):
  query = readFile(files[i])
  mergePairs.append(query)

writeFile(pathMerge, mergePairs)

