import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class Dense():
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.rand(n_inputs, n_neurons) * np.sqrt(2. / n_inputs)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, x):
        self.inputs = np.atleast_2d(x)
        self.output = np.dot(self.inputs, self.weights) + self.biases
        return self.output

    def backward(self, loss, learning_rate):
        loss = np.atleast_2d(loss)
        if self.inputs.shape[0] != loss.shape[0]:
            loss = loss.T
        self.weights_gradient = np.dot(self.inputs.T, loss)
        self.biases_gradient = np.sum(loss, axis=0, keepdims=True)
        self.input_gradient = np.dot(loss, self.weights.T)
        self.weights -= learning_rate * self.weights_gradient
        self.biases -= learning_rate * self.biases_gradient
        return self.input_gradient

class ReLU():
    def forward(self, x):
        self.input = x
        self.output = np.maximum(0, x)
        return self.output

    def backward(self, loss):
        loss = np.atleast_2d(loss)
        return loss * (self.input > 0)

def calculate_loss_gradient(y_pred, y_true):
    samples = len(y_pred)
    if len(y_pred.shape) == 1:
        y_pred = np.expand_dims(y_pred, axis=1)
    loss = (y_pred - y_true) / samples
    return loss

def mean_squared_error(y_pred, y_true):
    samples = len(y_pred)
    loss_gradient = calculate_loss_gradient(y_pred, y_true)
    loss = (loss_gradient ** 2) / samples
    return loss, loss_gradient

class Sequential():
    def __init__(self, layers, learning_rate):
        self.layers = layers
        self.lr = learning_rate

    def train(self, X_train, y_train, epochs):
        for _ in range(epochs):
            output = X_train
            for layer in self.layers:
                if isinstance(layer, ReLU):
                    output = layer.forward(output)
                else:
                    output = layer.forward(output)

            loss, loss_gradient = mean_squared_error(output, y_train)

            for layer in reversed(self.layers):
                if isinstance(layer, ReLU):
                    loss_gradient = layer.backward(loss_gradient)
                else:
                    loss_gradient = layer.backward(loss_gradient, self.lr)

            print(f"Epoch: {_+1} - Loss: {np.mean(loss)}")

    def predict(self, x):
        for layer in self.layers:
            if isinstance(layer, ReLU):
                x = layer.forward(x)
            else:
                x = layer.forward(x)
        return x

