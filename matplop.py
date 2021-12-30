'''
the problme
Using Numpy and Matplotlib, plot a figure of Gaussian distribution of mean=6.0, standard deviation=1.0, with size=100000
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(6.0, 1.0, 100000)
plt.hist(x, bins= 100)
plt.show()
