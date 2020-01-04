#!/usr/bin/python
import re
import numpy as np
from itertools import groupby
import json

def takeFile(pathFile):
  f = open(pathFile)
  txt = f.read()
  f.close()
  return txt

def removeTime(txt):
  replace1 = re.sub(r"\W[\d:\d]", "", txt)
  replace2 = re.sub(r"\d\d\W", "", replace1)
  result = replace2
  return result

def removeTab(txt):
  lineBreakTab = re.sub(r"\n \t", "\n", txt)
  firstLine = lineBreakTab.strip()
  result = firstLine
  return result

def uniqueName(arrName):
  arr = np.array(arrName)
  uniqName = np.unique(arr)
  return uniqName

txt = takeFile("../Jan/2-15.txt")
process1 = removeTime(txt)
process2 = removeTab(process1)
# print(process2)
# exit()

arrTxt = process2.splitlines()
# removeName = re.sub(r"^.*.\w: ", "", arrTxt[0])
getName = re.findall(r".*.\w+: ", process2)
# print(getName)
# exit()
uniqName = uniqueName(getName)
# print(uniqName[0])
# exit()
data={}
pattern1 = []
for index, msg in enumerate(arrTxt, start=1):
  getContent = re.sub(r"^.*.\w: ", "", msg)
  getName = re.findall(r".*.\w+: ", msg)

  if getName:
    conver={}
    label=""
    if getName[0] == uniqName[0]:
      label = "message"
    else:
      label = "response"

    conver = {label: getContent}
    pattern1.append(conver)

num=0
nextIndex=1
dataLength = len(pattern1)

# grouping same key 
pattern2 = []
index_pattern2 = 0
for index, arr in enumerate(pattern1, start=0):
  merge = (index_pattern2, arr.values()[0])
  pattern2.append(merge)

  if arr.keys() != pattern1[nextIndex].keys():
    index_pattern2+=1

  if index<dataLength-2:
    nextIndex+=1

pattern3 = []
objPattern3 = {}
for key, group in groupby(pattern2, lambda x: x[0]):
    listOfpattern2 = " ".join([pattern2[1] for pattern2 in group])
    pattern3.append(listOfpattern2)

question = []
answer = []
for key, chat in enumerate(pattern3, start=0):
  if key%2 == 0:
    question.append(chat)
  else:
    answer.append(chat)

datasets = []
# objData = {}
answerLen = len(answer)
for key, que in enumerate(question, start=0):
  # objData['message'] = que
  # if key<answerLen:
  #   objData['response'] = answer[key]
  # else:
  #   objData['response'] = ""
  
  # datasets.append(dict(objData))

  # berihkan tanda baca
  message = re.sub(r'[^\w\s]','',que)

  response = ""
  if key<answerLen:
    # bersihkan tanda baca
    response = re.sub(r'[^\w\s]','',answer[key])
  else:
    response = " "
  
  result = message+" ? <BOS>"+response+"<EOS>"
  print(result)
  datasets.append(result)

# print(datasets)
# write new file json
# with open('clean_1.json', 'w') as json_file:
#     json.dump(datasets, json_file)