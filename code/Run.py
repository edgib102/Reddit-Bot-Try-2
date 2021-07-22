from Scrape import getPost
from Image import construct_image, construct_title_image
from tts import create_tts, create_tts_title
from Edit import create_clip


print('started')
commentNames = []
ttsNames = []
title, commentList, authorlist, amount= getPost() #gets various varibles from Scrape.py

print(title)
create_tts_title(title,'TitleTtsAudio.mp3')
construct_title_image(title,'TitleImage.png')
print('created base title media')

for x in range(amount):
    commentName = f'Image{x}.png'
    ttsName = f'TtsAudio{x}.mp3'
    construct_image(commentList[x],authorlist[x],commentName) #tells Image.py to make an image with set comment and author (x is what comment to send)
    create_tts(commentList[x],ttsName) #tells tts.py to make an mp3 based off the comment set

    commentNames.append(commentName)
    ttsNames.append(ttsName)


create_clip(amount,ttsNames,commentNames)




