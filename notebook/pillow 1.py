from PIL import Image

path="/home/mato/opencv/data/lena.jpg"
im = Image.open(path)

print(im.size)
#size = (64,64) #썸네일 사이즈
#im.thumbnail(size) #썸네일 만들기
#512 5125 이미시 배열 사이즈 크기
#im.show()
#outpath="/home/mato/opencv/data/thumbnaillena.jpg"
#im.save(outpath)  #Make to Thumbnail

#outpath = "/home/mato/opencv/data/pillowlena.jpg"
# im.save(out.path) 이렇게하면 pillowlena.jpg 가 저장이 된다
# opencv 를 사용하지 않을때 PILLOW 라는 라이브러리를 자주 사용한다
