from background import removeBg
from localize_text import crop_and_display
from remove_bg import resizeImg
from find_face import find_face

 
img=removeBg('R14a.jpg')
croppedImg=resizeImg(img)
data=crop_and_display(croppedImg)
print(data)
find_face(img)
print(data)