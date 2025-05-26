import numpy as np
import matplotlib.pyplot as plt

class FunctionGrapher:
    def __init__(self, func, x_range):
        self.func = func
        self.x_range = x_range

    def plot(self):
        x_values = np.linspace(self.x_range[0], self.x_range[1], 1000)
        y_values = self.func(x_values)

        fig, ax = plt.subplots(figsize=(12, 12))
        ax.plot(x_values, y_values, label='f(x)', color='blue')
        ax.axhline(0, color='black', lw=1.5, ls='-')
        ax.axvline(0, color='black', lw=1.5, ls='-')
        ax.set_title('Graph of f(x)')
        plt.grid()
        plt.legend()

        plt.axis('equal')

        plt.show()

