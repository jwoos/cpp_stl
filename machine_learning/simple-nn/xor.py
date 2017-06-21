#!/usr/bin/env python3
# 3 layer neural network to figure out xor

import numpy as np

# 1 / (1 + e^(-x))
# s(x) * (1 - s(x)) where s(x) is the sigmoid function
# here, it can just use the input x, as it's being passed the calculated s(x)
def sigmoid(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

x = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

y = np.array([
    [0, 1, 1, 0]
]).T

np.random.seed(1)

syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for i in range(60000):
    layer0 = x
    layer1 = sigmoid(np.dot(layer0, syn0))
    layer2 = sigmoid(np.dot(layer1, syn1))

    layer2_error = y - layer2
    if (i % 10000) == 0:
        print('Error:', str(np.mean(np.abs(layer2_error))))

    layer2_delta = layer2_error * sigmoid(layer2, deriv=True)

    layer1_error = layer2_delta.dot(syn1.T)
    layer1_delta = layer1_error * sigmoid(layer1, deriv=True)

    syn1 += layer1.T.dot(layer2_delta)
    syn0 += layer0.T.dot(layer1_delta)

print('Output after training: ')
print(layer2)
