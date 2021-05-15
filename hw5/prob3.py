import random
import numpy as np

class MomentumNetwork(object):
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

  def SGD(self, training_data, epochs, mini_batch_size, lr, momentum, test_data=None):
    if test_data: n_test = len(test_data)
    n = len(training_data)
    for j in range(epochs):
      self.rng.shuffle(training_data)
      mini_batches = [
        training_data[k:k+mini_batch_size]
        for k in range(0, n, mini_batch_size)]
      for mini_batch in mini_batches:
        self.update_mini_batch(mini_batch, lr, momentum)
      if test_data:
        print("Epoch {0}: {1} / {2}".format(
          j, self.evaluate(test_data), n_test))
      else:
        print("Epoch {0} complete".format(j))

  def update_mini_batch(self, mini_batch, lr, momentum):
    nabla_b = [np.zeros(b.shape) for b in self.biases]
    nabla_w = [np.zeros(w.shape) for w in self.weights]
    momentum_b = [np.zeros(b.shape) for b in self.biases]
    momentum_w = [np.zeros(w.shape) for w in self.weights]
    momentum_const_b = [np.full(b.shape, momentum) for b in self.biases]  
    momentum_const_w = [np.full(w.shape, momentum) for w in self.weights]
    
    for x, y in mini_batch:
      delta_nabla_b, delta_nabla_w = self.backprop(x, y)
      nabla_b = np.array([nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)])
      nabla_w = np.array([nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)])
    
    # momentum_b = momentum * momentum_b + nabla_b
    # momentum_w = momentum * momentum_w + nabla_w
    momentum_b = [mcb * mc + nb
                    for mb, mcb, nb in zip(momentum_b, momentum_const_b, nabla_b)]
    momentum_w = [mcw * mw + nw
                   for mw, mcw, nw in zip(momentum_w, momentum_const_w, nabla_w)]
    
    self.weights = [w - (lr) * nw
                    for w, nw in zip(self.weights, momentum_w)]
    self.biases = [b - (lr) * nb
                   for b, nb in zip(self.biases, momentum_b)]

  def backprop(self, x, y):
      """Return a tuple ``(nabla_b, nabla_w)`` representing the
      gradient for the cost function C_x.  ``nabla_b`` and
      ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
      to ``self.biases`` and ``self.weights``."""
      nabla_b = [np.zeros(b.shape) for b in self.biases]
      nabla_w = [np.zeros(w.shape) for w in self.weights]
      # feedforward
      activation = x
      activations = [x] # list to store all the activations, layer by layer
      zs = [] # list to store all the z vectors, layer by layer
      for b, w in zip(self.biases, self.weights):
          z = np.dot(w, activation)+b
          zs.append(z)
          activation = sigmoid(z)
          activations.append(activation)
      # backward pass
      delta = self.cost_derivative(activations[-1], y) * \
        sigmoid_prime(zs[-1])
      nabla_b[-1] = delta
      nabla_w[-1] = np.dot(delta, activations[-2].transpose())
      # Note that the variable l in the loop below is used a little
      # differently to the notation in Chapter 2 of the book.  Here,
      # l = 1 means the last layer of neurons, l = 2 is the
      # second-last layer, and so on.  It's a renumbering of the
      # scheme in the book, used here to take advantage of the fact
      # that Python can use negative indices in lists.
      for l in range(2, self.num_layers):
        z = zs[-l]
        sp = sigmoid_prime(z)
        delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
        nabla_b[-l] = delta
        nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
      return (nabla_b, nabla_w)

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