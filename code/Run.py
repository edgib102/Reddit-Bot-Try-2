from Scrape import getPost

commentList, authorlist = getPost()

for comment in commentList:
    print(comment)