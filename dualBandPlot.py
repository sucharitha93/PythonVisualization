import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.cbook as cbook
import math


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
'''
interAPDistance = {}
def interAPDistanceCompute():	

	for ap1 in ['D1','D2','D3','D4','D5','D6','D7','D8']:
		for ap2 in ['D1','D2','D3','D4','D5','D6','D7','D8']:
			x1,y1 = routerCoordinates(ap1) 
			x2,y2 = routerCoordinates(ap2)
			distance = math.hypot(x2 - x1, y2 - y1)
			interAPDistance[ap1+" "+ap2] = distance

'''

#interAPDistanceCompute()

fieldnames = ['X', 'Y','D1','D2','D3','D4','D5','D6','D7','D8']
csvfile5GHz = open('5 LogDistance Refact.csv','r')
csvfile2GHz = open('2.4 LogDistance.csv','r')

#reader = csv.reader(csvfile, delimiter='\t')
image_file = cbook.get_sample_data(r'E:\AMuDA Lab\python code\1\testbed.png')
img = plt.imread(image_file)
fig,ax = plt.subplots(1)
ax.set_aspect('auto')
#ax.set_aspect('equal')
ax.imshow(img)

color = ['#ff0131','#00d980','#009afa','#fff800','k']

reader5GHz = csv.DictReader(csvfile5GHz,delimiter = ',')
reader2GHz = csv.DictReader(csvfile2GHz,delimiter = ',')
rc = 0
interAPDistance = {}

z = zip(reader2GHz,reader5GHz)

for row in z:
	d2 = {}	
	x,y = 0,0
	print(row)
	print(row[0])
	print(row[1])
	#break
	for k,v in row[0].items():
		
		if k in ['D1','D2','D3','D4','D5','D6','D7','D8'] and float(v) > 0.1:
			d2[k] = float(v)
		elif k == 'X':
			x = float(v)
		elif k == 'Y':
			y = float(v)
	sorted2GHz = sorted(d2.items(), key=lambda value: value[1])
	#print(sortE)

	d5 = {}

	for k5,v5 in row[1].items():
		
		if k5 in ['D1','D2','D3','D4','D5','D6','D7','D8'] and float(v5) > 0.1:
			d5[k5] = float(v5)
	sorted5GHz = sorted(d5.items(), key=lambda value: value[1])

	i = 0
	c=[]
	#print("##########################")

	#print(sorted2GHz,sorted5GHz)	


	for  itr in list(zip(sorted2GHz,sorted5GHz)):
		print(itr[0],itr[1])
		cir2= Circle((routerCoordinates(itr[0][0])),radius=float(itr[0][1]*10), color=color[i], fill=True, alpha = 0.2)
		c.append(cir2)
		ax.add_patch(cir2)
		cir5= Circle((routerCoordinates(itr[1][0])),radius=float(itr[1][1]*10), color=color[i], fill=True, alpha = 0.4)
		c.append(cir5)
		ax.add_patch(cir5)
		i = i + 1
		if i == 3:			
			rc = rc + 1
			circ = Circle((y,x),radius=float(1), color=color[4], fill=True, alpha = 0.5)
			ax.add_patch(circ)
			c.append(circ)
			plt.savefig(str(x)+'_'+str(y)+".png")
			for circle in c:
				circle.remove()
			
			break
	
	
				

	#break	
	
#print(rc)
csvfile2GHz.close()
csvfile5GHz.close()



		