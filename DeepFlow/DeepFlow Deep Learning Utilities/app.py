from DeepFlow import layers, models
from tensorflow.keras import datasets
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], -1).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0], -1).astype('float32') / 255

network = [
    layers.Dense(784, 128),
    layers.Relu(),
    layers.Dense(128, 10),
    layers.Softmax()
]

fnn = models.Sequential()
fnn.compile(learning_rate=0.5, loss="mean_squared_error", optimizer="mbgd")
accuracy, loss = fnn.fit(network, X_train, y_train, X_test, y_test, epochs=20)

def view_predictions(num):
    for i in range(num):
        prediction = fnn.predict(X_test[i])
        true_value = y_test[i]
        plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
        plt.title(f"Prediction: {prediction}, True Value: {true_value}")
        plt.show()
