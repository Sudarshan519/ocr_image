from rembg import remove
from PIL import Image
def removeBg(imgPath,newpath): 
    input = Image.open(imgPath)     
    path=newpath+'/removed.jpg'              
    output=remove(input)
    rgb_im = output.convert('RGB')
    rgb_im.save(path )
    return rgb_im