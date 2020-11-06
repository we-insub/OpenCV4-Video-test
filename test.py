import cv2
import glob
import os

path = "/home/mato/photo/"
src = glob.glob(path+'/*.jpg')  # list
# print(type(src), src)
counter = 0

for i in src:   # 파일 하나씩 읽어오기
    img = cv2.imread(i)
    #print(type(img))

    choice = input("파일에 넣을 효과 입력 (1:resize, 2:rotate, 3:blur, 4:crop) : ")
    actResize = '1' in choice
    actRotate = '2' in choice
    actBlur = '3' in choice
    catCrop = '4' in choice

    if actResize:
        # 기존 이미지의 크기 확인
        height, width, channel = img.shape
        print("height : {}, width : {}".format(height, width))

        # 기존 이미지의 2/1 크기로 변환
        dst_resize = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        height, width, channel = dst_resize.shape
        print("height : {}, width : {}".format(height, width))

        print(dst_resize.shape)
        cv2.imshow("after resize", dst_resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        dst = dst_resize
    if actRotate:
        # 기존 이미지의 크기 확인
        height, width, channel = dst.shape
        print("height : {}, width : {}".format(height, width))

        # 회전 중심, 회전각, scale
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
        dst_rotate = cv2.warpAffine(dst, matrix, (width, height))
        print(dst_rotate.shape)
        cv2.imshow("after rotate", dst_rotate)
        cv2.waitKey()
        cv2.destroyAllWindows()

        dst = dst_rotate
    if actBlur:
        # 흐릿하게 문대기
        # (4, 4)크기만큼 <-- 해당 숫자가 클 수록 더 흐릿하게 됨
        dst_blur = cv2.blur(dst, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
        print(dst_blur.shape)
        cv2.imshow("after blur", dst_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        dst = dst_blur
    if catCrop:
        # 기존 이미지의 크기 확인
        height, width, channel = dst.shape
        print("height : {}, width : {}, ch :{}".format(height, width, channel))
        dst_crop = dst[30:50, 30:50]
        # 작업 후 이미지의 크기 확인
        height, width, channel = dst_crop.shape
        print("height : {}, width : {}, ch :{}".format(height, width, channel))
        # print(dst_crop.shape)
        cv2.imshow("after crop", dst_crop)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        dst = dst_crop
    else:
        print("re-try")
        continue
    print('Done')

    # 이미지 저장하기
    dst_path = "/home/mato/photo/dogs.1.jpg"
    dst_name = "cg_dogs.%i" % counter + ".jpg"
    dst_fin = os.path.join(dst_path, dst_name)
    cv2.imwrite(dst_fin, dst)
    counter = counter + 1

    cv2.imshow("final image", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()