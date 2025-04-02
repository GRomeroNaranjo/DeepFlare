from regressions import Linear_Regression_Bivariate
import numpy as np

class Bivariate_Linear_Analysis:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.regression = None

    def line_best_fit(self):
        self.regression = Linear_Regression_Bivariate(self.x, self.y)
        self.regression.train(1000000)
        equation = self.regression.line_best_fit()
        return equation

    def correlation(self):
        x_array = np.array(self.x)
        y_array = np.array(self.y)
        corr_matrix = np.corrcoef(x_array, y_array)
        return corr_matrix[0, 1]

    def predict(self, x):
        if not self.regression:
            raise ValueError("Model has  not been set, run 'line_best_fit()' first.")
        return self.regression.predict(x)

    def full_analysis(self, configurations):
        line_best_fit = False
        corrcoef = None
        equation = None
        correlation_stated = False

        for configuration in configurations:
            if configuration.lower() == "line_best_fit":
                line_best_fit = True
            elif configuration.lower() == "correlation":
                corrcoef = self.correlation()
            elif configuration.lower() == "correlation-stated":
                corrcoef = self.correlation()
                correlation_stated = True
            else:
                raise ValueError(
                    "Invalid configuration."
                )

        if line_best_fit:
            equation = self.line_best_fit()
            self.regression.graph()

        corrcoef_described = None
        slope_described = None
        if correlation_stated:
            corrcoef1 = self.correlation()
            if corrcoef1 > 0.5 or corrcoef1 < -0.5:
                corrcoef_described = "strong"
            elif corrcoef1 < 0.1 and corrcoef1 > -0.1:
                corrcoef_described = "no"
            else:
                corrcoef_described = "weak"

            if self.regression.w > 0:
                slope_described = "positive"
            elif self.regression.w < 0:
                slope_described = "negative"

        correlation_description = f"{corrcoef_described} {slope_described} correlation"

        equation = str(equation) if equation else "Not calculated"
        corrcoef = str(corrcoef) if corrcoef is not None else "Not calculated"

        data = {
            "equation": equation,
            "correlation-coefficient": corrcoef,
            "correlation-described": correlation_description,
        }

        return data

y=[83, 59, 124, 120, 367, 439, 82]
x=[100, 9, 5000, 1500, 5000, 8000, 150]
data = Bivariate_Linear_Analysis(x, y)
data = data.full_analysis(["line_best_fit", "correlation-stated", "correlation-stated"])
print(data)

