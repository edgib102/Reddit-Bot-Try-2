from logging import exception
from os import close, replace
import praw
import json
import re

maxComments = 0

with open('swear_words.json') as x:
    swear_json = json.load(x)

#getting json file and opening it
with open('settings.json') as f:
    data = json.load(f)

#authentication
auth_data = data['auth']
reddit = praw.Reddit(
    client_id=auth_data['client_id'],
    client_secret=auth_data['client_secret'],
    user_agent=auth_data['user_agent']
)

print(reddit.read_only) #check to see if auth is working

def turn_to_json(submissions):
    jsonFile = open('prev_submissions.json', 'w')
    jsonString = json.dumps(submissions)
    jsonFile.write(jsonString)
    jsonFile.close()


def getPost():
    commentList = []
    authorList = []

    with open('prev_submissions.json', 'r') as x:
        global postList
        postList = json.load(x)
        print(postList)
        x.close()

    i=0
    reddit_details = data["reddit_details"]
    sub = reddit.subreddit(reddit_details["subreddit"])

    for submission in sub.hot(limit=None): #Gets submission/s from the set subreddit and loops per number of them
        i=0
        title = submission.title
        print(submission)

        if any(word in str(submission) for word in postList):
            print('post allready done')
            continue

        postList.append(str(submission))
        # if len(postList) >= 10:
        #     turn_to_json(postList)
        
        for comment in submission.comments: #loops x amount of comments from the submission
            # try:
            if comment.author is None:
                print('removed')
                continue
            commentList.append(comment.body)
            authorList.append(comment.author.name)
            i += 1

            if i == reddit_details['max_comments']: #if hit max comment amount it stops and returns information
                amount = len(commentList)
                turn_to_json(postList)
                return title, commentList, authorList, amount

            # except:
            #     print( + 'limit occured (take with grain of salt)')
            #     turn_to_json(postList)
            #     return title, commentList, authorList, amount

    amount = len(commentList)
    turn_to_json(postList)
    return title, commentList, authorList, amount

def reset_blacklist():
    postList = []

    jsonFile = open('prev_submissions.json', 'w')
    jsonString = json.dumps(postList)
    jsonFile.write(jsonString)
    jsonFile.close()
    




if __name__ == '__main__':
    # getPost()
    reset_blacklist()