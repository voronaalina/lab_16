import numpy as np
import pylab

data = np.loadtxt('data.txt')
flat_data = data.flatten()
unique_values, counts= np.unique(flat_data, return_counts=True)

pylab.bar(unique_values, counts)
pylab.xlabel("значення")
pylab.ylabel("частота")
pylab.title("гістограма частот значень масиву")
pylab.show()
