#!/usr/bin/env python3
# 2 layer neural network

import numpy as np

# 1 / (1 + e^(-x))
# s(x) * (1 - s(x)) where s(x) is the sigmoid function
# here, it can just use the input x, as it's being passed the calculated s(x)
def sigmoid(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# inputs
x = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

# expected value from the inputs
y = np.array([
    [0, 0, 1, 1]
]).T

# seed to be deterministic
np.random.seed(1)

# first layer of weights
syn0 = 2 * np.random.random((3, 1)) - 1

for i in range(10000):
    # layer 0 aka the inputs
    layer0 = x

    # layer 1
    layer1 = sigmoid(np.dot(layer0, syn0))

    layer1_error = y - layer1

    layer1_delta = layer1_error * sigmoid(layer1, deriv=True)

    # adjust the weights
    syn0 += np.dot(layer0.T, layer1_delta)

print('Output after training: ')
print(layer1)
