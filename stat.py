"""
the propblem
Given the list data= [15,18,13,20,20,11,14,99,100,200,201, 0], use
NumPy to calculate the mean, median, variance, and standard deviation
"""
import numpy as np
list_data= np.array([15,18,13,20,20,11,14,99,100,200,201,0])
print("The mean ia".format(list_data.mean()))
print("The median is".format(np.median(list_data)))
print("The variance is".format(np.var(list_data)))
print("The standard deviation is".format(np.std(list_data)))
