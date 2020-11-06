import numpy as np
import cv2

point = 0,0
#point 변수선언과 동시에 0,0으로 x,y초기화
def onMouse(event, x, y ,flags, action):
    # flags = 마우스 이벤트가 발생할때의 특정 조건
    global img # 아래 img 를 전역변수로 사용
    global point # 위에 point를 전역변수로 사용
    if event == cv2.EVENT_LBUTTONDOWN: # 만약 마우스 클릭 이벤트가 발생한다면,
        point=x,y # point 에 마우스 클릭값 x,y저장
    elif event == cv2.EVENT_LBUTTONUP: # 만약 마우스 클릭 해제 이벤트가 발생한다면,
        point1=x,y # point1 에 마우스 해제값 x,y저장
        cv2.rectangle(img,point,point1,(0,0,255),1)
        # 캔버스 마우스클릭좌표 마우스클릭해제좌표 Blue값으로 선두께1 데이터 표시
        # print(point,point1)
        font=cv2.FONT_HERSHEY_SIMPLEX
        # 입력할 Text의 폰트정하기
        text1='point=%s' % str(point) + 'point1=%s' %str(point1)
        # 문자1은 마우스클릭좌표와 마우스해제좌표의 x,y각각의 값을 문자열로 작성하여 저장한다

        if (point1[0] - point[0] < 0):
            # 버튼해제좌표 - 버튼클릭좌표 x값을 -했을때 0보다 크다면
            width = point[0] - point1[0] # 너비는 클릭좌표 x - 해제좌표 x의 값과 같다.
            pos_x = point1[0] # 그값을 pox_로 저장한다.
        else:
            width = point1[0] - point[0] # 해제좌표 x 에서 클릭좌표 x -뺸값은
            pos_x = point[0] # 그 값을 pos_x로 저장한다.

        if (point1[1] - point[1] < 0): # 해제좌표 y 에서 클릭좌표  y를 - 값이 0보다 크다면
            height = point[1] - point1[1] # 높이는 클릭좌표 y - 해제좌표 y를 한것은 높이이다
            pos_y = point1[1] # 그값을 pos_y로 저장한다.
        else:
            height = point1[1] - point[1] #높이는 해제좌표 y - 클릭좌표 y의 값을
            pos_y = point[1] # 클릭좌표의 y에 pos_y로 저장하여라

        org = (pos_x, pos_y - 10)  # 위의 조건문에서 저장된각각의 값에 -10을 하여라

        text2 = 'width=%s, ' % str(width) + 'height=%s' % height
        # int형 값을 문자열로 받아주는 작업
        # text2에서는 너비와 높이의 값을 저장한다.
        text=text1+text2
        # text1과 text2의 문자열을 합처준다
        print(text)
        # 문자열이 찍히게 print함수 사용
        cv2.putText(img, text, org, font, 1, (0, 255, 0), 2)
        # text를 집어넣는다. 이미지 출력문자 출력문자위치 글씨체 그린으로 글씨두께2
        cv2.imshow("img", action[0])
        # 캔버스에 action 자표값을 보여주세요
        # def 함수 끝

img =np.zeros((1200, 1600, 3), np.uint8)요
# 1200 1600 이 검은색으로 채워진 채널이 3개가 만들어진다
# 도화지의 색을 검은색으로 두기위해서 값을 입력하지않았다.
# 도화지의 색을 흰색으로 하고 싶다면, +255 배열에 255 값을 픽셀에 입력해서 흰색도화지가능
cv2.imshow('img', img)
# 이미지 전체캔버스 보여주세요
cv2.setMouseCallback('img', onMouse, [img])
# 전체 캔버스에 OnMouse함수 넣고,문자열이 저장된 캔버스(마우스이벤트) 정보를 저장합니다
cv2.waitKey() # 대기
cv2.destroyAllWindows() # 윈도우창 탈출