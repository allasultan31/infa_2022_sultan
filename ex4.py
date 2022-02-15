import numpy as np
import matplotlib.pyplot as plt


with plt.xkcd():
    x1 = np.arange(-10, 10, 0.01)
    x2 = eval(input("Введите функцию: "))
    plt.plot(x1, x2)

plt.show()