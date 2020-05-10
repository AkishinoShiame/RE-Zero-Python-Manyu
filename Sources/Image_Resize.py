import PIL
from PIL import Image

path = "C:/GitHub/Re-Zero-Python-Waza/tools/"
basewidth = 28

img = Image.open(path+'origional.jpg')

wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

img.save(path+'resized_picture.jpg')