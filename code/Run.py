from Scrape import getPost, reset_blacklist
from Image import construct_image, construct_title_image
from tts import create_tts, create_tts_title
from Edit import create_clip
from Upload import create_video
from Thumbnailx import create_thumbnail
from ProcessText import process_text

import json
from datetime import datetime, timedelta
import time

from PIL.Image import new

with open('settings.json') as f:
    settings = json.load(f)

videoAmount = settings['general_details']['video_amount']
bufferLength = settings['general_details']['buffer_length']
videoFileName = settings['video_details']['filename']
minUpvotes = settings['reddit_details']['min_upvotes']

print('started')
commentNames = []
ttsNames = []

startDatetime = datetime.now()
print('Started program at: ' + str(startDatetime))

def full():

    title, commentList, authorlist, upvoteList = getPost() #gets various varibles from Scrape.py

    if upvoteList.sort()[-1] <= minUpvotes:
        upvoteList

    commentList = process_text(commentList)
    amount = len(commentList)
    
    print(title)
    create_tts_title(title,'TitleTtsAudio.mp3')
    construct_title_image(title,'TitleImage.png')
    print('created base title media')

    create_thumbnail(title)
    print('created thumbnail')

    for x in range(amount):
        commentName = f'Image{x}.png'
        ttsName = f'TtsAudio{x}.mp3'

        if upvoteList.sort()[-1] <= minUpvotes:
            construct_image(commentList[x],authorlist[x],commentName) #tells Image.py to make an image with set comment and author (x is what comment to send)
        else:
            construct_image(commentList[x],authorlist[x],commentName,upvoteList[x])
        create_tts(commentList[x],ttsName) #tells tts.py to make an mp3 based off the comment set

        commentNames.append(commentName)
        ttsNames.append(ttsName)

    create_clip(amount,ttsNames,commentNames,videoFileName)

    create_video(videoFileName,'thumbnail.png',title,newTime)

    print('finished cycle at ' + str(datetime.now()))

i = 0

addTime = (24 / videoAmount) * 60
timeChange = timedelta(seconds=addTime)
newTime = startDatetime + timedelta(days=bufferLength)

maxtime = 0

while True:
    if i >= 10:
        break
    print('cycle' + str(i))
    i += 1

    newTime = newTime + timeChange
    newTime = newTime.replace(microsecond=0)
    full()
    
    time.sleep(addTime)
    maxtime += addTime
    if maxtime == 259200: #if 3 days worth of seconds have passed reset blacklist
        maxtime = 0
        reset_blacklist()



