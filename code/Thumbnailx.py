import PIL
from nltk.util import pr
from ScrapeImage import search_google
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageFilter
import textwrap
import os.path
import os
from textblob import TextBlob, blob
import json



OUTPUT_PATH = 'Thumbnail\\'
FONT_PATH ='Fonts\\'

fontSize = 115
fontPath = os.path.join(FONT_PATH,"Roboto-Bold.ttf")

size = (1920,1080)
TextColor = 'White'

with open('settings.json') as x:
    settings = json.load(x)

maxImageSearch = settings['general_details']['max_image_search']

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

def get_words(title):
    wordlist = ''
    blob = TextBlob(title)
    nouns = blob.noun_phrases
    for noun in nouns:
        wordlist += noun + ' '
    print(wordlist)
    blob = TextBlob(wordlist)
    # if wor
    return blob.words

def create_thumbnail(title):
    font = ImageFont.truetype(fontPath,fontSize)
    margin_x = 70
    margin_y = 150
    coloe = 20
    global imageList

    terms = get_words(title)

    # if len(terms):
    #     imageList = search_google(terms[int(len(terms)/2)] +' png', maxImageSearch)
    # else:
    #     imageList = search_google(title, maxImageSearch)

    imageList = ["Thumbnail\\search0.png"]

    transparent = False
    for googleScrapedImage in imageList:
        if has_transparency(googleScrapedImage) == True:
            transparent = True
            print(f"image has transparency")
            delete_images(googleScrapedImage)
            googleImage = Image.open(googleScrapedImage)            
            break
        else:
            transparent = False
        
    if transparent == False:
        if len(imageList) == 0:
            googleImage = Image.new('RGBA',size,(0,0,0,0))
        else:
            googleImage = Image.open(imageList[0])
            delete_images(imageList[0])

    mainImg = Image.new('RGB', size,(coloe,coloe,coloe))
    askredditLogo = Image.open(os.path.join(OUTPUT_PATH,'askreddit.png'))
    frame = Image.open(os.path.join(OUTPUT_PATH,'frame.png'))
 
    d = ImageDraw.Draw(mainImg)
    a = 1.1
    x = 750

    googleImage.thumbnail([x,x],Image.ANTIALIAS) #resises image to a controllable size

    askredditLogo = askredditLogo.resize((int(askredditLogo.width*a),int(askredditLogo.height*a)))

    width = (mainImg.width - googleImage.width) - 80
    height = (mainImg.height - googleImage.height) // 2

    with Image.open(os.path.join(OUTPUT_PATH,'mask.png')) as msk:
        # maskComposite = Image.new('RGBA', size,(coloe,coloe,coloe,coloe))
        
        mainImg.paste(googleImage,(width,height),googleImage)
        mainImg.paste(msk,(0,0),msk)
    
        mainImg.paste(googleImage,(width,height),googleImage)
        mainImg.paste(msk,(0,0),msk)
    
        # mainImg.show()

    mainImg.paste(frame,(0,0),frame)
    mainImg.paste(askredditLogo,(50,20),askredditLogo)

    textImg = Image.new('RGBA',size, (0,0,0,0)) 
    dt = ImageDraw.Draw(textImg)
    offset = (7,8)   
    # text_dimensions = get_text_size(title,font)

    dt.text((margin_x + offset[0],margin_y + offset[1]),textwrap.fill(title, width=17),fill='black',font=font)
    textImg = textImg.filter(ImageFilter.GaussianBlur(radius=2))


    mainImg.paste(textImg,(0,0),textImg)
    d.text((margin_x,margin_y),textwrap.fill(title, width=17),fill=TextColor,font=font)

    print('created thumbnail')
    
    mainImg.save(os.path.join(OUTPUT_PATH,'thumbnail.png'))


if __name__ == '__main__':
    create_thumbnail('Whats the most fucked up thing someone has ever said to you?')
    # get_words('People who stay awake late in the middle of the night, what are you doing?')


