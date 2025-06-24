from skimage.segmentation import felzenszwalb
from skimage.data import astronaut
from skimage.util import img_as_float
import matplotlib.pyplot as plt

image = img_as_float(astronaut())  
segments = felzenszwalb(image)
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(segments, cmap='copper')
plt.title("Segmented (Hierarchical)")
plt.show()

