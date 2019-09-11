import cv2
from PIL import Image
from mss import mss
import time
import numpy as np
import pytesseract
import serial

#image used for testing text recognition and image
#image = cv2.imread('TRAPPEDFULL.jpg')

#replace with port name
port = '/dev/cu.usbmodem14201'
ser = serial.Serial(port,9600) 
sct = mss()
#used for cooldown
previous_time = 0
#relace width and hight with screen resolution
width= 1400
height = 900
monitor = {'top': (height/5), 'left':(width/5)*2+50 , 'width': width/5-50, 'height': height/7}

#because this code is awful you need to use the keyboard inturpt CONT-C 
#or kill the process to end this loop, sorry
while True :
	
	


	#make this smaller will increase fps


	
	image = sct.grab(monitor)
	image = Image.frombytes("RGB", image.size, image.bgra, "raw", "BGRX")
	image = np.array(image)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	#uncomment to below line to save the last frame
	#cv2.imwrite('frame.jpg', image)
	


	# set blue and red channels to 0
	#image[:, :, 0] = 0
	#image[:, :, 2] = 0

#cv2.imwrite('G-RGB.jpg', g)
	rows,cols,_=image.shape
	for i in range(rows):
  		for j in range(cols):
  			px = image[i,j]
  			if px[1]<50 and px[2]>200:
  				image[i,j]=[0,0,0]
  			else:
  				image[i,j]=[255,255,255]



	#things to look for:
	#TRAPPED
	#SLEEP
	#PINNED
	#HACKED
	#STUNNED
	img = Image.fromarray(image)
	#img.save("toread.jpg")
	CC=["TRAPPED","SLEEP","PINNED","HACKED","STUNNED"]
	status=pytesseract.image_to_string(img)
	cur_time = time.time()
	for effect in CC:
		if effect in status:
			if curtime - previous_time > .5:
				ser.write(b'GO')
	previous_time = cur_time
	#uncomment the below break for testing
	#break



