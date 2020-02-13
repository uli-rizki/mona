#!/usr/bin/python

import numpy as np

# Number timestep in the input sequence
timesteps = 10
# Dimensionality of the input feature space
input_features = 32
# Dimensionality of the output feature space
output_features = 64

# Input data: random noise for the sake of the example
inputs = np.random.random((timesteps, input_features))
# Initial state: an all-zero vector
state_t = np.zeros((output_features,))

# Create random weight matrices
W = np.random.random((output_features, input_features))
U = np.random.random((output_features, output_features))
b = np.random.random((output_features,))

successive_outputs = []
for input_t in inputs:
  output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) + b)
  successive_outputs.append(output_t)

  state_t = output_t

final_output_sequence = np.concatenate(successive_outputs, axis=0)
print(final_output_sequence)