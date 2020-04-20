import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu, rank
from skimage.morphology import disk


def show_image(image, title):
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.title(title)
    plt.show()


def histogram(image):
    plt.hist(image, bins=256)
    plt.show()


#  show  image original
camera = data.page()
# show_image(camera, "Camera Original")

"""
show  thresholding otsu global
"""
thresh_global = threshold_otsu(camera)
camera_binary_global = camera > thresh_global
# show_image(camera_binary_global, "Camera Global")

# show histogram with line in thresh otsu
# plt.hist(camera.ravel(), bins=256)
# plt.axvline(thresh_global, color='r')
# plt.title('Histogram camera')
# plt.show()

"""
show  difference thresholding otsu local and global
"""

page = data.page()

# thresh local
radius = 17
thresh_local = rank.otsu(page, disk(radius))
page_thresh_local = page > thresh_local
# thresh global
thresh = threshold_otsu(page)
page_thresh_global = page > thresh

# show_image(page, "Page Original")
plt.subplot(221)
plt.imshow(page, cmap="gray")
plt.axis("off")
plt.title("page original")

# show histogram with line in thresh otsu
plt.subplot(222)
plt.hist(page.ravel(), bins=256)
plt.axvline(thresh_global, color='r')
plt.title('Histogram page')

plt.subplot(223)
plt.imshow(page_thresh_global, cmap="gray")
plt.axis("off")
plt.title("page global")

plt.subplot(224)
plt.imshow(page_thresh_local, cmap="gray")
plt.axis("off")
plt.title("page local")

plt.show()
