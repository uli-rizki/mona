#!/usr/bin/python

import numpy as np
from keras.datasets import imdb
from keras import preprocessing

def simple_one_hot_encoding():
  samples = ['The cat sat on the mat', 'The dog ate my homework']

  token_index = {}
  for sample in samples:
    for word in sample.split():
      if word not in token_index:
        token_index[word] = len(token_index) + 1

  max_length = 10

  results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))

  for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split())) [:max_length]:
      index = token_index.get(word)
      results[i, j, index] = 1
  
  return results

# print(simple_one_hot_encoding())

max_features = 1000
maxlen = 20

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = max_features)

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)

print(x_train)