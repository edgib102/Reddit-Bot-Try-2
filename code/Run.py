from Scrape import getPost
from Image import construct_image

title, commentList, authorlist, amount= getPost()
print(title)
for x in range(amount):
    print(commentList[x])




