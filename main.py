import json
import os
from background import removeBg
from localize_text import crop_and_display
from remove_bg import resizeImg
from find_face import find_face

imagepath="zOCR/rcs/r25a.jpg"
newpath=imagepath.split('.')[0]
if not os.path.exists(newpath):
    os.makedirs(newpath)


img=removeBg(imagepath,newpath)
croppedImg=resizeImg(img,newpath)
data=crop_and_display(newpath)
#  FIND and SAVE IMAGE
find_face(imagepath,newpath)

 # Write JSON data to file
file_path = newpath+'/data.json' 
json_data = json.dumps(data,  ensure_ascii=False)  # indent for pretty formatting
print(data)
with open(file_path, 'w') as file:
    file.write(json_data)

print(f"Dictionary written to {file_path}")