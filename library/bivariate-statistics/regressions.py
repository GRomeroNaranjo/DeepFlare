import matplotlib.pyplot as plt
import numpy as np

class Linear_Regression_Bivariate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = -0.763
        self.b = 0.343

    
    def train(self, epochs):
        lr=0.01
        for _ in range(epochs):
            for x, y in zip(self.x, self.y):
                output = self.w * x + self.b
                loss = (output - y)
                self.w = self.w - ((loss * x) * lr)
                self.b = self.b - (loss * lr)

    def line_best_fit(self):
        return f"y = {self.w}x + {self.b}", self.w, self.b
    
    def predict(self, x):
        return self.w * x + self.b
    
    def graph(self):
        plt.style.use("dark_background")
        fig, ax = plt.subplots()

        ax.scatter(self.x, self.y)
        ax.plot(self.x, [self.predict(i) for i in self.x])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Line-Best-Fit")

        ax.tick_params(colors="white")
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        

        return fig

class Quadratic_Regression_Bivariate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = -0.763
        self.b = 0.343
        self.c = 0.568

    def train(self, epochs):
        lr=0.01
        for _ in range(epochs):
            for x, y in zip(self.x, self.y):
                output = self.a * x ** 2 + self.b * x + self.c
                loss = (output - y)
                self.a = self.a - ((loss * x ** 2) * lr)
                self.b = self.b - ((loss * x) * lr)
                self.c = self.c - (loss * lr)


    def line_best_fit(self):
        return f"y = {self.a}x^2 + {self.b}x + {self.c}"
    
    def predict(self, x):
        return self.a * x ** 2 + self.b * x + self.c
    
    def graph(self):
        x_max = max(self.x)
        x_min = min(self.x)

        x_range = np.linspace(x_min, x_max, 100)
        x_range_list = x_range.tolist()
        y_pred = [self.predict(i) for i in x_range_list]

        plt.scatter(self.x, self.y, label="Data Points")
        plt.plot(x_range_list, y_pred, color='red', label="Best Fit Curve") 
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Quadratic Regression")
        plt.legend()
        plt.show()

class Cubic_Regression_Bivariate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = -0.763
        self.b = 0.343
        self.c = 0.568

    def train(self, epochs):
        lr=0.01
        for _ in range(epochs):
            for x, y in zip(self.x, self.y):
                output = self.a * x ** 3 + self.b * x + self.c
                loss = (output - y)
                self.a = self.a - ((loss * x ** 3) * lr)
                self.b = self.b - ((loss * x) * lr)
                self.c = self.c - (loss * lr)


    def line_best_fit(self):
        return f"y = {self.a}x^3 + {self.b}x + {self.c}"
    
    def predict(self, x):
        return self.a * x ** 3 + self.b * x + self.c
    
    def graph(self):
        x_max = max(self.x)
        x_min = min(self.x)

        x_range = np.linspace(x_min, x_max, 100)
        x_range_list = x_range.tolist()
        y_pred = [self.predict(i) for i in x_range_list]

        plt.scatter(self.x, self.y, label="Data Points")
        plt.plot(x_range_list, y_pred, color='red', label="Best Fit Curve") 
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Cubic Regression")
        plt.legend()
        plt.show()