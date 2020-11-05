import cv2

# 카메라 사용할 경우 파일 경로명을 입력해줘야 할 위치에
# 카메라 번호를 설정해주면 된다.
cap = cv2.VideoCapture(0)  # 0번은 노트북
# frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # cap.set 은 카메라에서만 가능하다
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 모든카메라가 가능한지는 확인해야한다.

frame_size = (frameWidth, frameHeight)
print('frame_size={}'.format(frame_size))

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
# 카메라 웹캠이 뜸