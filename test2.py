# import cv2
# import os
# img_path = "/home/kunalkatariya/MOT17/img1/"
# file_names = [f for f in sorted(os.listdir(img_path))]
# filename=img_path + file_names[0]
# img = cv2.imread(filename)
# cv2.rectangle(img,(912,484), (97,109),(0,255,0), 3)
# cv2.imshow("Image",img)
# cv2.waitKey(0)


x = []

for i in range(5):
    X = []
    X.append(i+1)
    X.append(i+2)
    X.append(i+3)
    x.append(X)

print(x[2][1])


#file_data = [line.split() for line in f]

# for i in file_data:
#             i = ''.join(i)
#             elements = i.split(",")
#             elements = ','.join(elements)
#             ele = elements.split(",")    
#             name_id = ele[1]

#             xmin = float(ele[2])
#             ymin = float(ele[3])
#             xmax = xmin + float(ele[4])
#             ymax = ymin + float(ele[5])
