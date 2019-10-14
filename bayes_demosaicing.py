from PIL import Image
import random

white = (255, 255, 255)

img = Image.new('RGB',(200,200), "white")

pixels = img.load()
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if i%2 == 0:
			if j%2 == 0:
				pixels[i,j] = (random.randint(-1,256), 0, 0)
			else:
				pixels[i,j] = (0,random.randint(-1,256), 0)
		else:
			if j%2 == 0:
				pixels[i,j] = (0,random.randint(-1,256), 0)
			else:
				pixels[i,j] = (0, 0, random.randint(-1,256))
img.show()

for i in range(1,img.size[0]-1):
	for j in range(1, img.size[1]-1):
		if i%2 == 0:
			if j%2 == 0:
				pixels[i,j] = (int(img.getpixel((i, j))[0]) , int((img.getpixel((i-1, j))[1]+img.getpixel((i+1, j))[1]+
								img.getpixel((i, j-1))[1]+img.getpixel((i, j+1))[1])/4) , int((img.getpixel((i+1, j+1))[2]+
								img.getpixel((i+1, j-1))[2]+img.getpixel((i-1, j+1))[2]+img.getpixel((i-1, j-1))[2])/4) )
			else:
				pixels[i,j] = ( int((img.getpixel((i-1, j))[0]+img.getpixel((i+1, j))[0])/2) , int((img.getpixel((i, j))[1]+
								img.getpixel((i-1, j-1))[1]+img.getpixel((i-1, j+1))[1]+img.getpixel((i+1, j+1))[1]+
								img.getpixel((i+1, j-1))[1])/5) , int((img.getpixel((i, j-1))[2]+img.getpixel((i, j+1))[2])/2) )
		else:
			if j%2 == 0:
				pixels[i,j] = ( int((img.getpixel((i-1, j))[0]+img.getpixel((i+1, j))[0])/2) , int((img.getpixel((i, j))[1]+
								img.getpixel((i-1, j-1))[1]+img.getpixel((i-1, j+1))[1]+img.getpixel((i+1, j+1))[1]+
								img.getpixel((i+1, j-1))[1])/5) , int((img.getpixel((i, j-1))[2]+img.getpixel((i, j+1))[2])/2) )
			else:
				pixels[i,j] = ( int((img.getpixel((i-1, j-1))[0]+img.getpixel((i-1, j+1))[0]+img.getpixel((i+1, j+1))[0]+
								img.getpixel((i+1, j-1))[0])/4) , int((img.getpixel((i-1, j))[1]+img.getpixel((i, j-1))[1]+
								img.getpixel((i+1, j))[1]+img.getpixel((i, j+1))[1])/4) , int(img.getpixel((i, j))[2]) )
img.show()
