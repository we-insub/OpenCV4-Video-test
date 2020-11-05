from PIL import Image

path="/home/mato/opencv/data/lena.jpg"

im=Image.open(path)
img2=im.rotate((90)) #반시계방향으로 90도 돈다
img2.show() # 리 사이즈