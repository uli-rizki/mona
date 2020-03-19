#!/usr/bin/python

from keras.models import load_model
from keras.optimizers import SGD

model = load_model('chatbot_model.h5')
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])