from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os.path
import json

#base text settings. Might change it into a json file if i can be fucked
FONT_PATH ='Fonts\\'
IMAGE_PATH='Video\\Image Bin'
font = os.path.join(FONT_PATH,"Roboto-Bold.ttf")
titleFont = os.path.join(FONT_PATH,"Roboto-Bold.ttf")

fontsize = 55
authorfontsize = 70
titleFontSize = 100
colorText = "white"
authorcolorText = "white"

with open('settings.json') as x:
    settings = json.load(x)


size = settings['video_details']['resolution']


def split_string(text, maxWords):
    words = text.split()
    wc = 0
    line = ''
    lines = []

    for word in words: #splits string into lines so they dont go off the screen.
        added = False
        wc += 1
        line += word + ' '
        if (wc % maxWords == 0 ):
            lines.append(line)
            line = ''
            added = True

    if (added is False):
        lines.append(line)
    
    return lines

def get_text_size(text_string, font):
    #returns text size. dont ask me how it works, because i dont know. it just does.
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    return (text_width, text_height)
        
def construct_image(text,author,name):
    #gets filepath where the image ends up and the name of the image
    filepath = os.path.join(IMAGE_PATH, name)
    #creates a blank transparent image
    img = Image.new('RGBA',size, (0,0,0,0))
    #opens up the image for editing
    d = ImageDraw.Draw(img)
    #sets fonts and font sizes
    commentFont = ImageFont.truetype(font, fontsize)
    authorFont = ImageFont.truetype(font, authorfontsize)
    #draws text onto the blank image we created earlier
    d.text((100,50),'u/'+author,font=authorFont,fill=authorcolorText) #Draws author text
    y = 250

    for line in split_string(text, 10):
        text_dimensions = get_text_size(line, commentFont) #gets text size
        x = (size[0] - text_dimensions[0]) / 2 #gets the center of the screen to place text to

        d.text((x, y),line,font=commentFont,fill=colorText) #draws text
        y += fontsize

    #saves the image at the set filepath
    img.save(filepath)
    print('made image')

    return()
        
def construct_title_image(text,name): #esentaly does the same thing as above exept with diff settings
    filepath = os.path.join(IMAGE_PATH, name)
    img = Image.new('RGBA',size, (0,0,0,0))
    d = ImageDraw.Draw(img)
    commentFont = ImageFont.truetype(font, titleFontSize)
    y = 250

    for line in split_string(text, 5):
        text_dimensions = get_text_size(line, commentFont)
        x = (size[0] - text_dimensions[0]) / 2

        d.text((x, y),line,font=commentFont,fill=colorText)
        y += titleFontSize+10

    #saves the image at the set filepath
    img.save(filepath)
    print('made image')

    return()


if __name__ == '__main__':
    construct_image('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','gamerboy','test.png')
    construct_title_image('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor','TitleTest.png')