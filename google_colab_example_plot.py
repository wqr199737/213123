# The code uses numpy to generate some random data, and uses matplotlib to visualize it. The plt.fill colorized the y axis values more than 195. 

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

# You are free to try and do anything extra in the google colab notebook
