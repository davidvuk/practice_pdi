import matplotlib.pyplot as plt


def show_image(image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()
