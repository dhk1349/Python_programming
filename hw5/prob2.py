import random
import numpy as np

class FTNetwork(object):
  def __init__(self, sizes):
    np.seterr(all='ignore')
    self.rng = np.random.RandomState(2021)
    self.num_layers = len(sizes)
    self.sizes = sizes
    self.biases = [self.rng.randn(y, 1) for y in sizes[1:]]
    self.weights = [self.rng.randn(y, x)
                    for x, y in zip(sizes[:-1], sizes[1:])]
      
  def feedforward(self, a):
    for b, w in zip(self.biases, self.weights):
      a = sigmoid(np.dot(w, a)+b)
    return a

  def SGD(self, training_data, epochs, mini_batch_size, lr, test_data=None, tuning=False):
    if test_data: n_test = len(test_data)
    n = len(training_data)
    for j in range(epochs):
      self.rng.shuffle(training_data)
      mini_batches = [
        training_data[k:k+mini_batch_size]
        for k in range(0, n, mini_batch_size)]
      for mini_batch in mini_batches:
        self.update_mini_batch(mini_batch, lr, tuning)
      if test_data:
        print("Epoch {0}: {1} / {2}".format(
          j, self.evaluate(test_data), n_test))
      else:
        print("Epoch {0} complete".format(j))

  def update_mini_batch(self, mini_batch, lr, tuning=False):
    pass

  def evaluate(self, test_data):
    test_results = [(np.argmax(self.feedforward(x)), y)
                   for (x, y) in test_data]
    return sum(int(x == y) for (x, y) in test_results)

  def cost_derivative(self, output_activations, y):
    return (output_activations-y)

def sigmoid(z):
  return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
  return sigmoid(z)*(1-sigmoid(z))
