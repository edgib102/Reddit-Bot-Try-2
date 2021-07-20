from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os.path

#base text settings. Might change it into a json file if i can be fucked
FONT_PATH =''
IMAGE_PATH='Image Bin'
fontname = "arial.ttf"
# fontname = "Lato-Regular.ttf"
fontsize = 11
colorText = "red"

def construct_image(text,author,name):
    #gets filepath where the image ends up and the name of the image
    filepath = os.path.join(IMAGE_PATH, name)
    #creates a blank transparent image
    img = Image.new('RGBA',(1920,1080), (0,0,0,0))
    #opens up the image for editing
    d = ImageDraw.Draw(img)
    #sets font and font size
    font = ImageFont.truetype(fontname, 55)
    #draws text onto the blank image we created earlier
    d.text((20,50), text, fill=colorText, font=font)
    #saves the image ot the set filepath
    img.save(filepath)

construct_image('test text','gamerboy','test.png')