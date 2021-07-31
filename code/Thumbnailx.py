from nltk.util import pr
from ScrapeImage import search_google
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
import os.path
import os
from textblob import TextBlob, blob

OUTPUT_PATH = 'Thumbnail\\'
FONT_PATH ='Fonts\\'

fontSize = 115
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

def get_words(title):
    wordlist = ''
    blob = TextBlob(title)
    nouns = blob.noun_phrases
    for noun in nouns:
        wordlist += noun + ' '
    print(wordlist)
    blob = TextBlob(wordlist)
    return blob.words



def create_thumbnail(title):
    font = ImageFont.truetype(fontPath,fontSize)
    margin_x = 70
    margin_y = 150
    coloe = 20
    global imageList

    terms = get_words(title)

    imageList = search_google(terms[int(len(terms)/2)] +' png',10)
    # imageList = ["Thumbnail\\search1.png"]
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
        
    # if transparent == False:
    #     imageNonTransparent = search_google(terms[int(len(terms)/2)],1,True)
    #     googleImage = Image.open(imageNonTransparent)
    if transparent == False:
        if len(imageList) == 0:
            googleImage = Image.new('RGBA',size,(0,0,0,0))
        else:
            googleImage = Image.open(imageList[0])
            delete_images(imageList[0])

    askredditLogo = Image.open(os.path.join(OUTPUT_PATH,'askreddit.png'))
    frame = Image.open(os.path.join(OUTPUT_PATH,'frame.png'))
    mainImg = Image.new('RGB', size,(coloe,coloe,coloe))
    
    

    d = ImageDraw.Draw(mainImg)
    d.text((margin_x,margin_y),textwrap.fill(title, width=17),fill=TextColor,font=font)    
    
    r = 1.5
    a = 1.1
    googleImage = googleImage.resize((int(googleImage.width*r),int(googleImage.height*r)))
    askredditLogo = askredditLogo.resize((int(askredditLogo.width*a),int(askredditLogo.height*a)))

    width = (mainImg.width - googleImage.width) - 80
    height = (mainImg.height - googleImage.height) // 2
    mainImg.paste(frame,(0,0),frame)
    mainImg.paste(askredditLogo,(50,20),askredditLogo)
    if transparent == False:
        mainImg.paste(googleImage,(width,height), googleImage)
    else:
        mainImg.paste(googleImage,(width,height))

    mainImg.save(os.path.join(OUTPUT_PATH,'thumbnail.png'))


if __name__ == '__main__':
    create_thumbnail('Redditors, how much cum did your father guzzle after raping you in the hallway?')
    # get_words('Redditors, how much cum did your father guzzle after raping you in the hallway?')

