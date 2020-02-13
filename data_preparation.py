#!/usr/bin/python
import os
import re
from itertools import groupby

def readFile(fileName):
  f = open(fileName)
  txt = f.read()
  f.close()
  return txt

def removeTab(txt):
  result = re.sub(r"\t", "", txt.strip())
  return result

def removeTime(txt):
  replace1 = re.sub(r"\W[\d:\d]", "", txt)
  replace2 = re.sub(r"\d\d\W", "", replace1)
  result = replace2
  return result

def uniqueName(names):
  listSet = set(names)
  uniqueList = (list(listSet))
  result = []
  for x in uniqueList:
    result.append(x)
  return result

def cleanUrl(string):
  result = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", string)
  return result

def cleanChar(string):
  result = re.sub(r'[^\w\s]','', string)
  return result

def processFile(fileName):
  fileContent = readFile(fileName)
  getLines = fileContent.splitlines()

  startConvers = 0
  endConvers = 0
  for i, lines in enumerate(getLines):
    if "Conversation started on" in lines:
      startConvers = i
    if "No tawk live chat account" in lines:
      endConvers = i

  listContent = []
  names = []
  for i, lines in enumerate(getLines):
    if startConvers < i < endConvers and lines.strip() and "GMT" not in lines and "has joined the conversation" not in lines:
      string = removeTime(lines)
      string2 = removeTab(string)
      listContent.append(string2)

      getName = re.findall(r".*.\w+: ", string2)
      if getName:
        names.append(getName[0])

  senders = uniqueName(names)

  # if listContent only 1
  if len(listContent) == 1:
    listContent.append('Admin: ')

  contents1 = []
  label = ""
  for i, content in enumerate(listContent):
    message = re.sub(r"^.*.\w: ", "", content)
    sender = re.findall(r".*.\w+: ", content)

    if sender:
      if sender[0] == senders[0]:
        label = "message"
      else:
        label = "response"
    else:
      label = label
    
    conver = {label: message}
    contents1.append(conver)
  
  contents2 = []
  idxContents2 = 0
  nextIndex = 1
  contentLength = len(contents1)
  for i, content in enumerate(contents1):
    merge = (idxContents2, content.values()[0])
    contents2.append(merge)

    if content.keys() != contents1[nextIndex].keys():
      idxContents2+=1
    
    if i < contentLength-2:
      nextIndex+=1

  contents3 = []
  for i, group in groupby(contents2, lambda x: x[0]):
    listOfcontents2 = " ".join([contents2[1] for contents2 in group])
    contents3.append(listOfcontents2)

  questions = []
  answers = []
  for i, conver in enumerate(contents3):
    if i%2 == 0:
      questions.append(conver)
    else:
      answers.append(conver)

  datasets = []
  answerLen = len(answers)
  for i, question in enumerate(questions):
    message = question
    message = cleanUrl(message)
    message = cleanChar(message)

    response = ""
    if i < answerLen:
      response = answers[i]
      response = cleanUrl(response)
      response = cleanChar(response)
    
    result = message + " ? " + response
    if (response):
      datasets.append(result)
  
  return datasets

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
'''
----------------------------------
Start Initialize File
----------------------------------
'''

path = "2018/April"
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if '.eml' in file:
      files.append(os.path.join(r, file))

file2Convert = ""
fileNum = 1
for i, f in enumerate(files):
  # file2Convert = files[54]
  datasets = processFile(files[i])
  newPath = "Merge/"+path
  fileName = newPath+"/"+str(fileNum)+".txt"
  createDir(newPath)

  if len(datasets) > 1:
    writeFile(fileName, datasets)
    fileNum+=1

# datasets = processFile(file2Convert)
# print(datasets)