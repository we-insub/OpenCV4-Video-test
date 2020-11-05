import cv2
import os

path = "/home/mato/opencv/data/lena.jpg"
# 동영상 파일이 있으면 읽어옴

if os.path.isfile(path):
    src = cv2.imread(path)
else:
    print("파일이 존재하지 않습니다.")

b,g,r = cv2.split(src)
height,width, channel = src.shape
print(height, width, channel)
#512 512 3 출력값
height,width = b.shape
print(height, width)
#512 512 채널이 한개짜리기 떄문에 이렇게 값이 나옴

# #도화지만들기
# zero = np.zeros((height, width, 1),dtype=np.uint8)
# #가로 세로 512 짜리를 0로 채워진 배열로 만드는것
# print(zero.shape)

imgB = cv2.merge((b,zero,zero))
imgG = cv2.merge((zero,g,zero))
imgR = cv2.merge((zero,zero,r))

cv2.imshow('b'.imgB)
cv2.imshow('b'.imgG)
cv2.imshow('b'.imgR)
cv2.waitKey()
cv2.destroyAllWindows()
