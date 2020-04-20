import matplotlib.pyplot as plt
from skimage import data, color, filters
import functions as fn


dados = plt.imread('img/dados.png')
# fn.show_image(dados)
dados_rgb = color.rgba2rgb(dados)
dados_gray = color.rgb2gray(dados_rgb)

dados_sobel = filters.sobel(dados_gray)
# fn.show_image(dados_sobel)


