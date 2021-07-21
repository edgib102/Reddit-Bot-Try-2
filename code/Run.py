from Scrape import getPost
from Image import construct_image
from tts import create_tts
from Edit import create_clip


print('started')

title, commentList, authorlist, amount= getPost() #gets various varibles from Scrape.py

print(title)
for x in range(amount):
    construct_image(commentList[x],authorlist[x],title,f'test{x}.png') #tells Image.py to make an image with set comment and author (x is what comment to send)
    create_tts(commentList[x],f'testA{x}.mp3') #tells tts.py to make an mp3 based off the comment set

create_clip(amount)




