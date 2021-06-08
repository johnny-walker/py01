import numpy as np
import cv2 

def imread_RGB(src):
    img = cv2.imread(src)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def filter2DBlur(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    kernel = np.ones((size, size), np.float32) / (size * size)
    dst = cv2.filter2D(img, -1, kernel) # 当ddepth=-1时，表示输出图像与原图像有相同的深度
    return dst


def averageBlur(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    dst = cv2.blur(img, (size, size))
    return dst


def gaussianBlur(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    dst = cv2.GaussianBlur(img,(size, size), 0)
    return dst

def medianBlur(args):
    size = args['kernel_size']
    img = imread_RGB(args['src'])
    dst = cv2.medianBlur(img, size)
    return dst