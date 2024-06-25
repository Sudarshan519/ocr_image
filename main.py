from background import removeBg
from localize_text import crop_and_display
from remove_bg import resizeImg
from find_face import find_face

imagepath="zOCR/r27a.png"
find_face(imagepath)
img=removeBg(imagepath)
croppedImg=resizeImg(img)
data=crop_and_display()
print(data)

print(data)