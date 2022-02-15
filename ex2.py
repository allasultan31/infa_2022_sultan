import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 15, 0.01)
plt.plot(x,  x*x - x - 6)
plt.show()