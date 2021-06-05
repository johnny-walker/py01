#https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

import numpy as np
import cv2 
from matplotlib import pyplot as plt

def imread_RGB(src):
    img = cv2.imread(src)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def show_diff(img, dst):
    plt.subplot(121), plt.imshow(img), plt.title('Image 1')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Image 2')
    plt.xticks([]), plt.yticks([])
    plt.show()


def blur_filter2D(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    kernel = np.ones((size, size), np.float32) / (size * size)
    dst = cv2.filter2D(img, -1, kernel) # 当ddepth=-1时，表示输出图像与原图像有相同的深度
    if args['show']:
        show_diff(img, dst)
    return dst


def blur_average(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    dst = cv2.blur(img, (size, size))
    if args['show']:
        show_diff(img, dst)
    return dst


def blur_gaussian(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    dst = cv2.GaussianBlur(img,(size, size), 0)
    if args['show']:
        show_diff(img, dst)
    return dst


if __name__ == '__main__':
    args = {}
    args['src'] = 'data/dog.jpeg'
    args['kernel_size'] = 19
    args['show'] = True

    img1 = blur_filter2D(args)
    #img2 = blur_average(args)
    #img2 = blur_gaussian(args)

    #show_diff(img1, img2)