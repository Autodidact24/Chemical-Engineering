import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

tap = Image.open(sys.argv[1]).convert('L')
tap_a = np.array(tap)

tap_g = ndimage.gaussian_filter(tap_a, 1)
tap_norm = (tap_g - tap_g.min())/(float(tap_g.max()) - tap_g.min())
tap_norm[tap_norm < 0.5] = 0
tap_norm[tap_norm >= 0.5] = 1

result = 255 - (tap_norm * 255).astype(np.uint8)

tap_labeled, count = ndimage.label(result)

plt.imshow(tap_labeled)
plt.show()
