from PIL import Image
import cv2
path="/home/mato/opencv/data/lena.jpg"

im=Image.open(path)
img2=im.resize((800,800)) #튜플형 자료 넣기
img2.show() # 리 사이즈

#dst=cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
#Open CV 를 통해서 resize하는 방법