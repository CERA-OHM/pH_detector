# pip install pandas opencv-python

import cv2
import pandas as pd

# --------------------------------------------------------------------------

img_path = 'chart.jpg'
csv_path = 'colors.csv'

# reading csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B', 'pH']
df = pd.read_csv(csv_path, names=index, header=None)

# reading image
img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

#declaring global variables
clicked = False
#r = g = b = xpos = ypos = 0
r = g = b = xpos = ypos = ph = 0


#function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname


#function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

# creating window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
	cv2.imshow('image', img)
	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
		cv2.rectangle(img, (0,20), (800,60), (b,g,r), -1)

		#Creating text string to display( Color name and RGB values )
		#text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		if r <= 10 and g <= 185 and b <= 184:
			ph = 9
			type = "Weak Alkali"
		elif r <= 35 and g <= 181 and b <= 108:
			ph = 8
			type = "Neutral"
		elif r <= 49 and g <= 172 and b <= 74:
			ph = 7
			type = "Neutral"
		elif r <= 55 and g <= 85 and b <= 164:
			ph = 11
			type = "Weak Alkali"
		elif r <= 70 and g <= 44 and b <= 131:
			ph = 14
			type = "Strong Alkali"
		elif r <= 71 and g <= 145 and b <= 205:
			ph = 10
			type = "Weak Alkali"
		elif r <= 75 and g <= 185 and b <= 72:
			ph = 6
			type = "Neutral"
		elif r <= 90 and g <= 82 and b <= 163:
			ph = 12
			type = "Strong Alkali"
		elif r <= 98 and g <= 70 and b <= 156:
			ph = 13
			type = "Strong Alkali"
		elif r <= 132 and g <= 195 and b <= 65:
			ph = 5
			type = "Weak Acid"
		elif r <= 183 and g <= 212 and b <= 51:
			ph = 4
			type = "Weak Acid"
		elif r <= 238 and g <= 29 and b <= 36:
			ph = 0
			type = "Strong Acid"
		elif r <= 242 and g <= 103 and b <= 36:
			ph = 1
			type = "Strong Acid"
		elif r <= 244 and g <= 237 and b <= 27:
			ph = 3
			type = "Weak Acid"
		elif r <= 251 and g <= 201 and b <= 21:
			ph = 2
			type = "Strong Acid"
		else:
			ph = " - "
			type = "Not in Range"

		text = get_color_name(r,g,b) + ' pH=' + str(ph) + ' ' + type

		#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

		#For very light colours we will display text in black colour
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()

