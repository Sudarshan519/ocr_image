from background import removeBg
from localize_text import crop_and_display
from remove_bg import resizeImg
from find_face import find_face

imagepath="ImportedPhoto_1711430511856.jpg"
find_face(imagepath)
img=removeBg(imagepath)
croppedImg=resizeImg(img)
data=crop_and_display()
print(data)

print(data)