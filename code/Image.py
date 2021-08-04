from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
from PIL import ImageFilter
import os.path
import json

#base text settings. Might change it into a json file if i can be fucked
FONT_PATH ='Fonts\\'
IMAGE_PATH='Video\\Image Bin'
EFFECT_PATH = 'Video\\Effects'
font = os.path.join(FONT_PATH,"Roboto-Bold.ttf")
titleFont = os.path.join(FONT_PATH,"Roboto-Bold.ttf")

fontsize = 55
authorfontsize = 70
authorfontsize2 = 55
titleFontSize = 100
colorText = "white"
authorcolorText = "white"

with open('settings.json') as x:
    settings = json.load(x)

size = settings['video_details']['resolution']
minUpvotes = settings['reddit_details']['min_upvotes']

offset = (5,5)
dropshadowImg = Image.new('RGBA',size, (0,0,0,0)) 
def create_dropshadow(text,textFont,pos):
    dropshadowImg = Image.new('RGBA',size, (0,0,0,0)) 
    dr = ImageDraw.Draw(dropshadowImg)

    dr.text((pos[0] + offset[0],pos[1] + offset[1]),text,font=textFont,fill='black')
    # dropshadowImg_blur = dropshadowImg.filter(ImageFilter.GaussianBlur(radius=2))
    return dropshadowImg

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
        
def construct_image(text,author,name,upvotes=0):
    # dropshadowImg = Image.new('RGBA',size, (0,0,0,0)) 
    dropshadowImg = Image.new('RGBA',size, (0,0,0,0))     
    #gets filepath where the image ends up and the name of the image
    filepath = os.path.join(IMAGE_PATH, name)
    dr = ImageDraw.Draw(dropshadowImg)
    #creates a blank transparent image
    img = Image.new('RGBA',size, (0,0,0,0))
    #opens up the image for editing
    d = ImageDraw.Draw(img)
    #sets fonts and font sizes
    commentFont = ImageFont.truetype(font, fontsize)
    authorFont = ImageFont.truetype(font, authorfontsize)
    authorFont2 = ImageFont.truetype(font, authorfontsize2)
    #draws text onto the blank image we created earlier

    authx = 100
    authy = 50

    # create_dropshadow(f'u/{author}',authorFont,(authx,authy))
    dr.text((authx + offset[0],authy + offset[1]),f'u/{author}',font=authorFont,fill='black')   
    d.text((authx,authy),f'u/{author}',font=authorFont,fill=authorcolorText) #Draws author text

    if upvotes >= 1:
        text_dimensions = get_text_size(f'u/{author}',authorFont)

        dr.text((text_dimensions[0] + authx + offset[0],authy+ 10 + offset[1]),f' • {upvotes}',font=authorFont2,fill='black')
        d.text((text_dimensions[0] + authx,authy+10),f' • {upvotes}', font=authorFont2) # draws upvote text

        with Image.open(os.path.join(EFFECT_PATH,'Upvote arrow.png')) as im: #pastes arrow
            text_dimensions2 = get_text_size(f' • {upvotes}',authorFont2)
            img.paste(im,(text_dimensions[0] + text_dimensions2[0] + authx + 10,72),im)            

        with Image.open(os.path.join(EFFECT_PATH,'Upvote arrow dr.png')) as im: #pastes dropshadow arrow

            dropshadowImg.paste(im,(text_dimensions[0] + text_dimensions2[0] + authx + 10 + offset[0],72 + offset[1]),im)

        with Image.open(os.path.join(EFFECT_PATH,'bar.png')) as im: #pastes seperation bar
            img.paste(im,(0,0),im)
        
        with Image.open(os.path.join(EFFECT_PATH,'frame2.png')) as im: #pastes frame
            img.paste(im,(0,0),im)

    y = 250

    for line in split_string(text, 10):
        text_dimensions = get_text_size(line, commentFont) #gets text size
        x = (size[0] - text_dimensions[0]) / 2 #gets the center of the screen to place text to

        # dropshadowImg = create_dropshadow(line,commentFont,(x,y))
        dr.text((x + offset[0],y + offset[1]),line,font=commentFont,fill='black')
        d.text((x, y),line,font=commentFont,fill=colorText) #draws text
        y += fontsize

    dropshadowImg_blur = dropshadowImg.filter(ImageFilter.GaussianBlur(radius=5))

    
    dropshadowImg_blur.paste(img,(0,0),img)
    
    
    #saves the image at the set filepath
    # dropshadowImg_blur.show()
    red = Image.new('RGB',size, (255,0,0,0))
    red.paste(dropshadowImg_blur,(0,0),dropshadowImg_blur)
    red.show()
    red.save(filepath)
    print('made image')
    dropshadowImg = Image.new('RGBA',size, (0,0,0,0)) 
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
    # dropshadowImg.show()
    # img.save(filepath)
    print('made image')

    return()


if __name__ == '__main__':
    construct_image('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','gamerboy08','test.png',305)
    construct_image('epic gamer','skerrr69696969','test.png',0)
    construct_title_image('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor','TitleTest.png')