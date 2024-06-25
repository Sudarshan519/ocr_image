from rembg import remove
from PIL import Image
def removeBg(imgPath): 
    input = Image.open(imgPath)                   
    output=remove(input)
    rgb_im = output.convert('RGB')
    rgb_im.save('removed.jpg')
    return rgb_im