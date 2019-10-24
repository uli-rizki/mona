#!/usr/bin/python

flag = True

while flag == True :
  sentence = raw_input("User : ")
  if sentence == "quit" :
    exit()
  else :
    response = sentence.lower()
    print "Mona :", response