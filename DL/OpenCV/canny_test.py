import sys
import numpy as np
import cv2

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.Canny(src, 50, 100)
dst2 = cv2.Canny(src, 50, 200)
dst3 = cv2.Canny(src, 100, 200)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()

cv2.destroyAllWindows()