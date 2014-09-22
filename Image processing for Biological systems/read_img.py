import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi

img = np.flipud(plt.imread('bubbles.jpg'))
img_clean = img[:880, :]
img_med = ndi.median_filter(img_clean, size=5)
plt.imshow(img_med, cmap=plt.cm.gray, interpolation='nearest')
plt.hist(img_med.flat, bins=40, range=(0, 1000))

bubbles = (img_med <= 50)
sand = (img_med > 50) & (img_med <= 120)
glass = (img_med > 120)


def plot_images(cmap=plt.cm.gray):
    for n, (name, image) in \
        enumerate([('Original', img_med),
                   ('Bubbles', bubbles),
                   ('Sand', sand),
                   ('Glass', glass)]):

        plt.subplot(2, 2, n + 1)
        plt.imshow(image, cmap=cmap)
        plt.title(name)
        plt.axis('off')


def plot_color_overlay():
    all_layers = np.zeros((img_clean.shape[0],
                           img_clean.shape[1], 3)) # Color image

    assert(bubbles.dtype == np.bool)

    all_layers[bubbles] = (1, 0, 0)
    all_layers[sand] = (1, 1, 0)
    all_layers[glass] = (0, 0, 1)

    plt.imshow(all_layers)


if __name__ == '__main__':
    #plot_color_overlay()
    plot_images()
    plt.show()
