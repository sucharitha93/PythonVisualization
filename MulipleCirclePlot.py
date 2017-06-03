import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.cbook as cbook
import math

interAPDistance = {}
#to plot use x,y as y,x 
routerCoordinates = {(110,90),(110,320),(240,390),(268,264),(220,177),(270,15),(422,320),(422,90)}

def routerCoordinates(index):
	if index == "D1":
		x,y = 110,320
	elif index == "D2":
		x,y = 110,90
	elif index == "D3":
		x,y = 240,390
	elif index == "D4":
		x,y = 268,264
	elif index == "D5":
		x,y = 220,177
	elif index == "D6":
		x,y = 270,15
	elif index == "D7":
		x,y = 422,320
	elif index == "D8":
		x,y = 422,90
	else:
		x,y = 0,0
	return y,x

def interAPDistanceCompute():	

	for ap1 in ['D1','D2','D3','D4','D5','D6','D7','D8']:
		for ap2 in ['D1','D2','D3','D4','D5','D6','D7','D8']:
			x1,y1 = routerCoordinates(ap1) 
			x2,y2 = routerCoordinates(ap2)
			distance = math.hypot(x2 - x1, y2 - y1)
			interAPDistance[ap1+" "+ap2] = distance

interAPDistanceCompute()

fieldnames = ['X', 'Y','D1','D2','D3','D4','D5','D6','D7','D8']
csvfile = open('Data.csv','r')

#reader = csv.reader(csvfile, delimiter='\t')
image_file = cbook.get_sample_data(r'E:\AMuDA Lab\python code\1\testbed.png')
img = plt.imread(image_file)
fig,ax = plt.subplots(1)
ax.set_aspect('auto')
#ax.set_aspect('equal')
ax.imshow(img)

color = ['r','g','y','pink','b']

reader = csv.DictReader(csvfile,delimiter = ',')
rc = 0
interAPDistance = {}
for row in reader:	
	d = {}
	
	
	x,y = 0,0
		

	for k,v in row.items():

		
		if k in ['D1','D2','D3','D4','D5','D6','D7','D8'] and float(v) > 0.1:
			d[k] = float(v)
		elif k == 'X':
			x = float(v)
		elif k == 'Y':
			y = float(v)
	sortE = sorted(d.items(), key=lambda value: value[1])
	#print(sortE)


	i = 0
	t = []
	ti = []
	c=[]

	for  k,v in sortE:
		t.append(v)
		ti.append(k)		
		print(t[i])
		circ= Circle((routerCoordinates(ti[i])),radius=float(t[i]*10), color=color[i], fill=True, alpha = 0.5)
		c.append(circ)
		ax.add_patch(c[i])
		i = i + 1
		if i == 4:
			circ = Circle((y,x),radius=float(1), color=color[i], fill=True, alpha = 0.5)
			ax.add_patch(circ)
			c.append(circ)
			plt.savefig(str(x)+'_'+str(y)+".png")
			rc = rc + 1
			for circle in c:
				circle.remove()
			break	

	#break	
	
#print(rc)
csvfile.close()


		