#https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html

import argparse
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

def check_dir(filepath):
    separators = os.path.split(filepath)
    if separators:
        dir = filepath.replace(separators[-1], '')
        if not os.path.isdir(dir):
            os.mkdir(dir)
            print('create folder:', dir)


def imread_RGB(src):
    img = cv2.imread(src)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def imwrite(path, img):
    img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, img_BGR)
    print(img_BGR.shape)

def show_one(dst):
    plt.xticks([]), plt.yticks([])
    plt.imshow(dst)
    plt.show()

def show_diff(img, dst):
    plt.subplot(121), plt.imshow(img), plt.title('Image 1')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Image 2')
    plt.xticks([]), plt.yticks([])
    plt.show()


def resize(args):
    img = imread_RGB(args.src)

    dst = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
    ''' 
    height, width = img.shape[:2]
    dst = cv2.resize(img, (width//4, height//4), interpolation = cv2.INTER_CUBIC)
    '''

    show_diff(img, dst)
    return dst


def translate(args):
    img = imread_RGB(args.src)
    rows, cols = img.shape[:2]

    # [ 1, 0, tx
    #   0, 1, ty ]
    M = np.float32( [[1, 0, args.tx], [0, 1, args.ty]] )
    '''
    src – 输入图像。
    M – 变换矩阵。
    dsize – 输出图像的大小。
    '''
    dst = cv2.warpAffine(img, M, (cols,rows))

    show_diff(img, dst)
    return dst


def rotate(args, image=None):
    if type(image) is np.ndarray:
        img = image
    else:
        img = imread_RGB(args.src)
    rows, cols = img.shape[:2]

    '''
    center：图片的旋转中心
    angle：旋转角度
    scale：旋转后图像相比原来的缩放比例
    M:计算得到的旋转矩阵
    '''
    M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), args.angle, args.scale)
    dst = cv2.warpAffine(img, M, (cols,rows))
    if args.show:
        show_diff(img, dst)
        #show_one(dst)
    return dst


def animate_rotate(args):
    img = cv2.imread(args.src)
    args.show = False

    # 讓視窗可以自由縮放大小
    height, width = img.shape[:2]
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    while True:
        dst = rotate(args, img)
        cv2.imshow('frame', dst)
        cv2.resizeWindow('frame', (width//2, height//2))
        args.angle +=  1 % 360
        key = cv2.waitKey(33)
        # ESC
        if key == 27:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', default='data/dog.jpeg', help="source file")
    parser.add_argument('--show', action='store_true', help="source file")
    parser.add_argument('--tx', type=int, default=200, help='horizontal translation') 
    parser.add_argument('--ty', type=int, default=150, help='veritcal translation') 
    parser.add_argument('--angle', type=int, default=10, help='rotation angle') 
    parser.add_argument('--scale', type=float, default=0.5, help="scale ratio") 
    parser.add_argument('--output', default='output/output.png', help="output result") 
    parser.add_argument('--save', default=True, help="save result") 
    args = parser.parse_args()

    img = None
    #img = resize(args)
    img = translate(args)
    #img = rotate(args)
    animate_rotate(args)

    if args.save and img is not None:
        destination = args.output
        check_dir(destination)
        imwrite(destination, img)
        print("save file under: ", args.output)