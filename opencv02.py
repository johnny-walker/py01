import numpy as np
import cv2
from matplotlib import pyplot as plt

# 使用 OpenCV 讀取圖檔
# OpenCV 讀取進來的圖片會以 BGR 的方式儲存三個顏色的 channel
img = cv2.imread('data/dog.jpeg')

# 將 BGR 圖片轉為 RGB 圖片
img = img[:,:,::-1]
# 或是這樣亦可
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片 : RGB方式儲存三個顏色的 channel
plt.imshow(img)
plt.show()
