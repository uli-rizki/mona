#!/usr/bin/python

import nltk
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
# from keras.optimizers import SGD
from keras.optimizers import RMSprop
import random

words=[]
context = []
response_1 = []
response_0 = []
data_file = open('intents.json').read()
intents = json.loads(data_file)


for intent in intents['intents']:
  # take each word and tokenize it
  ctx = intent['context']
  w = nltk.word_tokenize(ctx)
  words.extend(w)
  context.append(ctx)
  response_0.append(intent['response_0'])
  response_1.append(intent['response_1'])

words = sorted(list(set(words)))
# pickle.dump(words,open('words.pkl','wb'))

# # initializing training data
training = []
for i, ctx in enumerate(context):
  bag = []
  bag_0 = []
  bag_1 = []
  for w in words:
    bag.append(1) if w in ctx else bag.append(0)
    bag_0.append(1) if w in response_0[i] else bag_0.append(0)
    bag_1.append(1) if w in response_1[i] else bag_1.append(0)
  training.append([bag, bag_0, bag_1])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])
train_z = list(training[:,2])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_z[0]), activation='softmax'))
model.summary()

  