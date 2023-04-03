import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst1 = np.zeros(src.shape[:2], np.uint8)
_, dst1 = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)

dst2 = np.zeros(src.shape[:2], np.uint8)
_, dst2 = cv2.threshold(mag, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()