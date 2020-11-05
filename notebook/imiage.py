import cv2
import os

path = "/home/mato/opencv/data/lena.jpg"
# 동영상 파일이 있으면 읽어옴

if os.path.isfile(path):
    gray = cv2.imread(path, 0)
else:
    print("파일이 존재하지 않습니다.")

imgBGR = cv2.merge((gray, gray, gray))

cv2.imshow('imgRGB', imgBGR)
cv2.imshow('gray', gray)

cv2.waitKey()
cv2.destroyAllWindows()