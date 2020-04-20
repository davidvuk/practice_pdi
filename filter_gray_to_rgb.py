import matplotlib.pyplot as plt
from skimage.color.adapt_rgb import adapt_rgb, each_channel
from skimage.filters import sobel


img = plt.imread('img/lena.png')
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.axis("off")


@adapt_rgb(each_channel)
def sobel_rgb(image):
    return sobel(image)


plt.subplot(122)
plt.imshow(sobel_rgb(img), cmap="gray")
plt.axis("off")
plt.show()
