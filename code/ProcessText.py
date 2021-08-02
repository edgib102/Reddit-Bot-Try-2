import json
from better_profanity import profanity

with open('settings.json') as x:
    settings = json.load(x)

with open('word_blacklist.json') as x:
    wordBlacklist = json.load(x)

blacklist = wordBlacklist['words']
maxChars = settings['text_details']['max_chars']

profanity.load_censor_words_from_file('swear_words.txt')
textList = []

def process_text(baseTextList):
    for text in baseTextList:
        if len(text) >= maxChars:
            print('above max char limit')
        elif any(word in text for word in blacklist):
            print('Blacklisted comment')
        else:
            textList.append(text)
        
    for text in textList:
        censored_text = profanity.censor(text)
        print(censored_text)
    return textList

    
if __name__ == '__main__':
    x = process_text(['edit:car if','bitch you fuck'])
    # print(x)
