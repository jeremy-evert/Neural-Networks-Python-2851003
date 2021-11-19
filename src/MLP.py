import numpy as np
import math

class Perceptron:
    """A single neuron with the sigmoid activation function.
       Attributes:
          inputs: The number of inputs in the perceptron, not counting the bias.
          bias:   The bias term. By defaul it's 1.0."""

    def __init__(self, inputs, bias = 1.0):
        """Return a new Perceptron object with the specified number of inputs (+1 for the bias)."""
        self.weights = (np.random.rand(inputs+1) * 2) - 1
        self.bias = bias

    def set_weights(self, w_init):
        self.weights = np.array(w_init)


    def sigmoid(self,sum):
        return 1/(1+np.exp(-sum))


    def run(self, x):
        """Run the perceptron. x is a python list with the input values."""
        sum = np.dot(np.append(x,self.bias),self.weights)
        return self.sigmoid(sum)
