import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow_pyplot(argv=None):
    print('OpenCV 版本:',cv2.__version__)

    img = cv2.imread(argv)
    # 將 BGR 圖片轉為 RGB 圖片
    img = img[:,:,::-1]

    # 使用 Matplotlib 顯示圖片
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    imshow_pyplot('data/dog.jpeg')