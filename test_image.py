import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('test.png')

imgplot = plt.imshow(img)
plt.show()