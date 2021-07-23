from ScrapeImage import search_google
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
import os.path
import os

OUTPUT_PATH = 'Thumbnail\\'
FONT_PATH ='Fonts\\'

fontSize = 100
fontPath = os.path.join(FONT_PATH,"Roboto-Bold.ttf")

size = (1920,1080)
TextColor = 'White'

def delete_images(imgExclude):
     for image in imageList:
         if image == imgExclude:
             continue
         os.remove(image)

def has_transparency(imgPath): #someone else's code, idk how it works 
    img = Image.open(imgPath)
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False

def create_thumbnail(title):
    font = ImageFont.truetype(fontPath,fontSize)
    margin_x = 70
    margin_y = 100
    
    mainImg = Image.new('RGB', size)

    d = ImageDraw.Draw(mainImg)
    
    d.text((margin_x,margin_y),textwrap.fill(title, width=20),fill=TextColor,font=font)
    global imageList
    imageList = search_google('dog png',5)

    for googleScrapedImage in imageList:
        if has_transparency(googleScrapedImage) == True:
            print(f"image has transparency")
            delete_images(googleScrapedImage)
            break

            # googleImage = Image.open(googleScrapedImage)

    # img.show()


if __name__ == '__main__':
    create_thumbnail('Redditors, how much of your cum did your father guzzle after raping you in the hallway?')

