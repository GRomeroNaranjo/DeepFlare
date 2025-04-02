class MinMaxScaler:
    def __init__(self, array):
        self.min = min(array)
        self.max = max(array)
        self.range = self.max - self.min if self.max != self.min else 1

    def transform(self, array):
        return [(i - self.min) / self.range for i in array]

    def inverse(self, array):
        return [i * self.range + self.min for i in array]        