from os import close, replace
import praw
import json
import re

maxComments = 0

with open('swear_words.json') as x:
    swear_json = json.load(x)

#getting json file and opening it
with open('requirements.json') as f:
    data = json.load(f)

#authentication
auth_data = data['auth']
reddit = praw.Reddit(
    client_id=auth_data['client_id'],
    client_secret=auth_data['client_secret'],
    user_agent=auth_data['user_agent']
)

print(reddit.read_only) #check to see if auth is working

def getPost():
    commentList = []
    authorList = []
    i=0
    reddit_details = data["reddit_details"]
    sub = reddit.subreddit(reddit_details["subreddit"])
    for submission in sub.hot(limit=(reddit_details["post_limit"])):
        i=0
        i2 = 0
        for comment in submission.comments:
            try:
                # for word in swear_json['base']['swear_words']:
                # currentComment = "nigger"#str(comment.body)

                # big_regex = re.compile('|'.join(map(re.escape, swear_json['base']['swear_words'])))
                # checkedComment = big_regex.sub("repl-string", currentComment)

                # # for swearWord in swear_json['base']['swear_words']:
                # #     checkedComment = currentComment.replace(swearWord, swear_json['base']['replacement_words'][i2])
                # #     i2 += 1
                # # checkedAccount = comment.author.replace("fuck", "f*ck")
                commentList.append(comment)
                authorList.append(comment.author)
                print(checkedComment)
                print()
                i += 1
                if i == reddit_details['max_comments']:
                    return commentList, authorList
            except AttributeError:
                print(AttributeError)
                return commentList, authorList

    return commentList, authorList

getPost()
print("Finished scalping reddit")