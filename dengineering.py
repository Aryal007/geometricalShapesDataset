import numpy as np
import os
import math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFilter


alpha = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
             "A", "B", "C", "D", "E", "F")

def randbetween(n1,n2):
	return np.random.random_integers(low=n1,high=n2,size=None)

def randcolor():
	random = np.random.random_integers(10)

	if random%3 == 0:	#One third of the generated shapes have fill and background
		return '#'+''.join([np.random.choice(alpha) for _ in range(6)])
	else:
		return '#FFFFFF'

def polygon(sides, radius=1, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides

    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]

    if translation:
        points = [[sum(pair) for pair in zip(point, translation)]
                  for point in points]

    return points

#Creating Circles
def createcircles():
	#first 1000 circles with noise and distortion
	for i in range(1000):
		x2=randbetween(160,180)
		y2=randbetween(160,180)
		x1=randbetween(1,20)
		y1=randbetween(1,20)

		image = Image.new('RGBA', (200, 200),randcolor())
		draw = ImageDraw.Draw(image)
		draw.ellipse((x1, y1, x2, y2), fill = randcolor(),outline = '#000000')
		image=image.filter(ImageFilter.GaussianBlur(2))
		image.save('./data_geometricalshapes/circles//'+str(i)+'tt.jpeg')

	#second 1000 circles
	for i in range(1000,2000):
		x=randbetween(160,180)
		y=randbetween(160,180)
		t=randbetween(160,180)
		u=randbetween(1,20)
		c=randcolor()
		image = Image.new('RGBA', (200, 200),c)
		draw = ImageDraw.Draw(image)
		draw.ellipse((t, u,x, y), fill = c,outline ='#000000')
		image.save('./data_geometricalshapes/circles//'+str(i)+'tt.jpeg')
		#remaining circles
	for i in range(2000,5000):
	    x=np.random.random_integers(low=50,high=200,size=None)
	    t=np.random.random_integers(low=1,high=20,size=None)
	    v=randcolor()
	    w=randcolor()
	    z=randcolor()
	    image = Image.new('RGBA', (200,200),v)
	    draw = ImageDraw.Draw(image)
	    draw.ellipse((t,t,x,x), fill = w,outline = '#000000')
	    image.save('./data_geometricalshapes/circles//'+str(i)+'tt.jpeg')

#Creating Triangles
def createtriangles():
	for i in range(5000,10000):
	    im = Image.new('RGB', (200, 200))
	    draw = ImageDraw.Draw(im)
	    x1=randbetween(0,200)
	    x2=randbetween(0,200)
	    x3=randbetween(0,200)
	    y1=randbetween(0,200)
	    y2=randbetween(0,200)
	    y3=randbetween(0,200)
	    v=randcolor()
	    v_=randcolor()
	    draw.polygon([(0, 0), (0, 200), (200, 200), (200, 0)], fill = v, outline='#000000')
	    if i<9000:
	        draw.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = v, outline='#000000') 
	        im.save('./data_geometricalshapes/triangles//'+str(i)+'tt.jpeg')
	    else:
	        draw.polygon([(x1,y1), (x2, y2), (x3,y3)], outline='#000000',fill = v) 
	        im.save('./data_geometricalshapes/triangles//'+str(i)+'tt.jpeg')

#Creating Rectangles
def createrectangles():
	for i in range(10000,15000):
	    im = Image.new('RGB', (200, 200))
	    draw = ImageDraw.Draw(im)
	    x1=randbetween(0,100)
	    x2=randbetween(100,200)
	    x4=x1
	    x3=x2
	    y1=randbetween(0,110)
	    y3=randbetween(90,200)
	    y2=y1
	    y4=y3
	    v=randcolor()
	    v_=randcolor()
	    draw.polygon([(0, 0), (0, 200), (200, 200), (200, 0)], fill = v, outline='#000000')
	    draw.polygon([(x1,y1), (x2, y2), (x3,y3),(x4,y4)], fill = v, outline='#000000')
	    if i<14000:
	        draw.polygon([(x1,y1), (x2, y2), (x3,y4),(x4,y3)], fill = v, outline='#000000')
	        im.save('./data_geometricalshapes/rectangles//'+str(i)+'tt.jpeg')
	    else:
	        draw.polygon([(x1,y1), (x2, y2), (x3,y4),(x4,y3)], outline='#000000',fill = v) 
	        im.save('./data_geometricalshapes/rectangles//'+str(i)+'tt.jpeg')

#Creating pentagons
def createpentagons():
	for i in range(15000,20000):
	    im = Image.new('RGB', (200, 200))
	    draw = ImageDraw.Draw(im)
	    r=randbetween(50,100)
	    t1=randbetween(90,110)
	    t2=randbetween(90,110)
	    t3=randbetween(90,110)
	    angle=randbetween(0,360)
	    pg=polygon(5,radius=r,rotation=angle,translation=(t1,t2,t3))

	    v=randcolor()
	    v_=randcolor()
	    draw.polygon([(0, 0), (0, 200), (200, 200), (200, 0)], fill = v, outline='#000000')

	    if i<19000:
	        draw.polygon([tuple(pg[0]),tuple(pg[1]),tuple(pg[2]),tuple(pg[3]),tuple(pg[4])],fill =v, outline='#000000')
	        im.save('./data_geometricalshapes/pentagons//'+str(i)+'tt.jpeg')
	    else:
	        draw.polygon([tuple(pg[0]),tuple(pg[1]),tuple(pg[2]),tuple(pg[3]),tuple(pg[4])], outline='#000000',fill =v)
	        im.save('./data_geometricalshapes/pentagons//'+str(i)+'tt.jpeg')

##write main remaining
def main():
	
	try:
		os.makedirs('./data_geometricalshapes')
		os.makedirs('./data_geometricalshapes/triangles')
		os.makedirs('./data_geometricalshapes/rectangles')
		os.makedirs('./data_geometricalshapes/circles')
		os.makedirs('./data_geometricalshapes/pentagons')
	except:
		print("Error Occured")
		exit(0)
	
	createcircles()
	createtriangles()
	createpentagons()
	createrectangles()
	
if __name__=="__main__":
	main()



