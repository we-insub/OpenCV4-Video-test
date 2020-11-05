from PIL import Image

path="/home/mato/opencv/data/lena.jpg"

im=Image.open(path)
img2=im.crop((100,100, 350,350)) #튜플형 자료 넣기 100 100에서 350 350 만큼잘라라
img2.show() # 리 사이즈