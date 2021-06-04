import numpy as np 
import cv2 

# 讀取圖檔

img = cv2.imread('data/dog.jpeg')
cv2.imshow('My Image', img)

#img_gray = cv2.imread('data/dog.jpeg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('My Image2', img_gray)

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()


# 寫入圖檔
# 寫入不同圖檔格式
cv2.imwrite('output/output.png', img)
#cv2.imwrite('output/output.tiff', img)

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
#cv2.imwrite('output/output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
#cv2.imwrite('output/output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])
