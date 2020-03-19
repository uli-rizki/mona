#!/usr/bin/python
import os
import re
import json

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
path = "../Datasets/may.txt"

pairs = readFile(path)
pairs2list = pairs.split('\n')

pairsJson = []
for item in pairs2list:
  itemSplit = item.split('?')
  if len(itemSplit) > 1:
    pairsObj = {"message": itemSplit[0], "response": itemSplit[1]}

  pairsJson.append(pairsObj)

with open('may.json', 'w') as f:
    json.dump(pairsJson, f)