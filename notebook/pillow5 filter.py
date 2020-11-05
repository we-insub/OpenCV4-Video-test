from PIL import Image, ImageFilter

path="/home/mato/opencv/data/lena.jpg"

im=Image.open(path)
img2=im.filter(ImageFilter.BLUR) #튜플형 자료 넣기 100 100에서 350 350 만큼잘라라
img2.show() # 리 사이즈

open cv를 이용한 블러처리
