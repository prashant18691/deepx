import theano.tensor as T

from ..node import Node

class Linear(Node):
    def __init__(self, n_in, n_out):
        super(Linear, self).__init__(n_in, n_out)

        self.W = self.init_parameter('W', (n_in, n_out))
        self.b = self.init_parameter('b', n_out)

    def activate(self, X):
        return X

    def _forward(self, X):
        return self.activate(T.dot(X, self.W) + self.b)

class Softmax(Linear):

    def activate(self, X):
        if X.ndim <= 2:
            e_x = T.exp((X - X.max(axis=1)[:, None]))
            return e_x / e_x.sum(axis=1)[:, None]
        e_x = T.exp((X - X.max(axis=2)[:, :, None]))
        return e_x / e_x.sum(axis=2)[:, :, None]

class Sigmoid(Linear):

    def activate(self, X):
        return T.nnet.sigmoid(X)

class Tanh(Linear):

    def activate(self, X):
        return T.tanh(X)

class Relu(Linear):

    def activate(self, X):
        return T.nnet.relu(X)