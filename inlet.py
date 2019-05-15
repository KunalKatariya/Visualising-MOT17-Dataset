import os
import argparse
import time
import pprint

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

import json
import cv2

parser = argparse.ArgumentParser(description='Evaluate label Converting.')
parser.add_argument('--img_path', type=str, help='directory of image folder')
parser.add_argument('--label_path', type=str, help='directory of label folder')
parser.add_argument('--img_type', type=str, help='type of image', default='.jpg')


args = parser.parse_args()

img_path = args.img_path
label_path = args.label_path
img_type = args.img_type

data = None
result = None

        

   

data = {}

f = open("/home/kunalkatariya/MOT17/gt/gt.txt", "r")

file_data = [line.split() for line in f]


img_width = str(1920)
img_height = str(1080)
img_depth = 3

size = {
"width": img_width,
"height": img_height,
"depth": img_depth
}

obj = {}
obj_cnt = 0
xmin = []
xmax = []
ymin = []
ymax = []
count = 1

# [[Foo() for x in range(10)] for y in range(10)]

# [[]]
count=0
for i in range(601):
    temp =[]
    temp2 = []
    temp3 = []
    temp4 = []
    xmin.append(temp)
    ymin.append(temp2)
    xmax.append(temp3)
    ymax.append(temp4)

for i in file_data:
    i = ''.join(i)
    elements = i.split(",")
    elements = ','.join(elements)
    ele = elements.split(",")    
    name_id = ele[1]
    yy = float(ele[3]) + float(ele[5])
    xx = float(ele[2]) + float(ele[4])
    xmin[int(ele[0])].append(float(ele[2]))
    ymin[int(ele[0])].append(float(ele[3]))
    xmax[int(ele[0])].append(yy)
    ymax[int(ele[0])].append(xx)
    

   
 ########################################  
file_names = [f for f in sorted(os.listdir(img_path))]
count = 1

for i in range(len(file_names)):
    filename=img_path + file_names[i]
    print(filename)
    #reading each files
    img = cv2.imread(filename)
    for j in range(len(xmin[count])):
        cv2.rectangle(img,(int(xmin[count][j]),int(ymin[count][j])), (int(ymax[count][j]),int(xmax[count][j])),(0,255,0), 3)
        print("xmin", xmin[count][j])
        print("ymin", ymin[count][j])
        print("xmax", xmax[count][j])
        print("ymax", ymax[count][j])   
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    img = cv2.resize(img, (960, 540))  
    cv2.imshow("Image",img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    count=count+1
    print("===============================================================================================\n\n")
cv2.destroyAllWindows()



