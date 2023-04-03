import numpy as np
import cv2

src = cv2.imread('pinkwink_namecard.png')

w, h = 720, 400    # 바꾸고 싶은 사이즈

srcQuad = np.array([
    [212, 110], [539, 157], [546, 340], [143, 274] # 명함의 4개 좌표
], np.float32)

dstQuad = np.array([
    [0,0], [w-1,0], [w-1,h-1], [0,h-1]
], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w,h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()