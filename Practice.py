#사진 한장을 가지고
# Riseze
# Rotate
# Blur
# Crop
# 만들어보기 .패스 ,아웃패스 이용 , 트루 폴스 이용해서 값
# actResize = T/F
# actRotate = T/F
# if actResize :
# cv2.resize(path) 이런식트리 하나의변수에서 실행한 변수의 값을 다음으로 잘 이어주기

import cv2
# 리사이즈
src = cv2.imread("/home/mato/photo/dogs.1.jpg", cv2.IMREAD_COLOR)
dst = cv2.resize(src, dsize=(100, 100), interpolation=cv2.INTER_AREA)
# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 각 4개의 변수가 참인지 거짓인지 어떻게 알지? 그렇다면,
# input으로 1,0을 받아서 사용해보자 a을 input로 선언
# 화면에 나타나는 윈도우 종 cv2.destroyAllWindows()

a=int(input("사진크기변경 = 1 / 원본 = 0 입력하시오 : "))
actResize = a
if actResize == 1:
    dst
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    src
    cv2.imshow("src", src)
    cv2.waitKey()
    cv2.destroyAllWindows()

b=int(input("사진회전 = 1 / 원본 = 0 입력하시오 : "))
actRotate=b
if actRotate == 1:
    height, width, channel = src.shape
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
    dst = cv2.warpAffine(src, matrix, (width, height))
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    src
    cv2.imshow("src", src)
    cv2.waitKey()
    cv2.destroyAllWindows()

c=int(input("사진블러처리 = 1 / 원본 = 0 입력하시오 : "))
actBlur = c
if actBlur ==1:
    dst = cv2.blur(src, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    src
    cv2.imshow("src", src)
    cv2.waitKey()
    cv2.destroyAllWindows()

d=int(input("사진자르기 = 1 / 원본 = 0 입력하시오 : "))
actCrop = d
if actCrop == 1:
    dst = src[100:600, 200:700]
    cv2.imshow("dst", dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    src
    cv2.imshow("src", src)
    cv2.waitKey()
    cv2.destroyAllWindows()
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()

# #로테이션
# src = cv2.imread("/home/mato/photo/dogs.1.jpg", cv2.IMREAD_COLOR)
#height, width, channel = src.shape
#matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
#dst = cv2.warpAffine(src, matrix, (width, height))
# #cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 블러 처리
# path = "/home/mato/photo/dogs.1.jpg"
# src = cv2.imread(path)
# dst1 = cv2.blur(src, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("dst1", dst1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#크롭
# path = "/home/mato/photo/dogs.1.jpg"
# src = cv2.imread(path)
# dst = src.copy()
# dst = src[100:600, 200:700]
# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()