import cv2
import numpy as np

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])

dst = cv2.filter2D(src, -1, kernel)
dst_blur = cv2.blur(src, (3,3))

cv2.imshow('src', src)
cv2.imshow('dst_mean', dst)
cv2.imshow('dst_blur', dst_blur)

cv2.waitKey()

cv2.destroyAllWindows()