import cv2
import os
path= '/home/mato/opencv/data'
filePath= os.path.join(path,"vtest.avi")
print(filePath)
#경로설정
if os.path.isfile(filePath):
    cap = cv2.VideoCapture(filePath)
else:
    print("파일이 존재하지 않습니다.")

# 동영상 크기(frame정보)를 읽어옴

frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_size = (frameWidth, frameHeight)
print('frame_size={}'.format(frame_size))

# 동영상 프레임을 캡쳐

frameRate = 33

while True:
    # 한 장의 이미지를 가져오기
    # 이미지 -> frame
    # 정상적으로 읽어왔는지 -> retval
    retval, frame = cap.read()
    if not (retval):
        break  # 프레임정보를 정상적으로 읽지 못하면 while문을 빠져나가기

    cv2.imshow('frame', frame)
    key = cv2.waitKey(frameRate)  # frameRate msec동안 한 프레임을 보여준다

    # 키 입력을 받으면 키값을 key로 저장 -> esc == 27
    if key == 27:
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()