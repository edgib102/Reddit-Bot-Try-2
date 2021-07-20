from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os.path

# def create_image(text,author,name):

FONT_PATH =''
IMAGE_PATH='Image Bin'

fontname = "arial.ttf"
# fontname = "Lato-Regular.ttf"
fontsize = 11
text = "example@gmail.com"
colorText = "red"

file = os.path.join(IMAGE_PATH, 'test.png')

# font_file = os.path.join(FONT_PATH, fontname)


img = Image.new('RGBA',(1920,1080), (0,0,0,0))
d = ImageDraw.Draw(img)
font = ImageFont.truetype(fontname, 55)

d.text((20,50), text, fill=colorText, font=font)
img.save(file)