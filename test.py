import os
from PIL import Image

img_path = "/home/kunalkatariya/MOT17/img1/"
#img_type = ".jpg"
file_names = os.path.abspath(img_path)
for file_name in file_names:

    #txt = open(os.path.join(img_path, file_name), "r")

    file_name = file_name.split(".")[0]
    print(file_name)
    #img = Image.open(os.path.join(img_path, "".join([file_name, img_type])))

       