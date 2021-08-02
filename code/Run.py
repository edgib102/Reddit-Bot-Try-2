from nltk.util import pr
from Scrape import getPost, reset_blacklist
from Image import construct_image, construct_title_image
from tts import create_tts, create_tts_title
from Edit import create_clip
from Upload import create_video
from Thumbnailx import create_thumbnail
import time

videoName = 'Reddit Tts video.mp4'

print('started')
commentNames = []
ttsNames = []

def full():

    title, commentList, authorlist, amount= getPost() #gets various varibles from Scrape.py

    print(title)
    create_tts_title(title,'TitleTtsAudio.mp3')
    construct_title_image(title,'TitleImage.png')
    print('created base title media')

    create_thumbnail(title)
    print('created thumbnail')

    for x in range(amount):
        commentName = f'Image{x}.png'
        ttsName = f'TtsAudio{x}.mp3'
        construct_image(commentList[x],authorlist[x],commentName) #tells Image.py to make an image with set comment and author (x is what comment to send)
        create_tts(commentList[x],ttsName) #tells tts.py to make an mp3 based off the comment set

        commentNames.append(commentName)
        ttsNames.append(ttsName)

    create_clip(amount,ttsNames,commentNames,videoName)

    create_video(videoName,'thumbnail.png',title)

    print('finished cycle at ' + time.ctime())

i = 0
addTime = 3000
maxtime = 0
while True:
    if i >= 10:
        break
    print('cycle' + str(i))
    i += 1

    full()
    time.sleep(addTime)
    maxtime += addTime
    if maxtime == 259200: #if 3 days worth of seconds have passed reset blacklist
        maxtime = 0
        reset_blacklist()



