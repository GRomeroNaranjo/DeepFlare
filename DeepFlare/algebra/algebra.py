import math
import numpy as np
import matplotlib.pyplot as plt

def factor_quadratic(a, b, c):
    output_1 = -b + math.sqrt((b ** 2) - 4 * a * c) / 2 * a
    output_2 = -b - math.sqrt((b ** 2) - 4 * a * c) / 2 * a
    if output_1 < 0:
        output_1 = f"- {output_1}"
    else:
        output_1 = f"+ {output_1}"

    if output_2 < 0:
        output_2 = f"- {output_2}"
    else:
        output_2 = f"+ {output_2}"

    return f"(x {output_1})(x {output_2})"

class linear_equation():
    def __init__(self, x, y, x_1, y_1):
        self.x = x
        self.y = y
        self.x_1 = x_1
        self.y_1 = y_1

    def equation(self):
        if self.x > self.x_1:
            m = (self.y - self.y_1) / (self.x - self.x_1)
        elif self.x_1 > self.x:
            m = (self.y_1 - self.y) / (self.x_1 - self.x)
        else:
            raise ValueError("Invalid input. Please input two distinct points.")
        
        a = m
        b = -m * self.x + self.y
        self.m = a
        self.b = b
        return f"y = {a}x + {b}", a, b
    
    def predict(self, x):
        return self.m * x + self.b

    def graph(self):
        equation, _, _ = self.equation()
        
        x_values = np.linspace(-100, 100, 500)
        y_values = [self.predict(x) for x in x_values]

        plt.plot(x_values, y_values, label=equation)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        plt.xlabel("X")
        plt.ylabel("Y")
        
        plt.title(f"Graph of {equation}")
        plt.legend()
        plt.grid(True)
        plt.show()

def graph(predict_function, equation):
    predict = predict_function   
            
    x_values = np.linspace(-100, 100, 500)
    y_values = [predict(x) for x in x_values]

    plt.plot(x_values, y_values, label=equation)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.title(f"Graph of {equation}")
    plt.legend()
    plt.grid(True)
    plt.show()

