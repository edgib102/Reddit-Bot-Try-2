import pyttsx3
import os.path
engine = pyttsx3.init()
engine.setProperty('rate',400)
baseFilepath = 'Video\\Tts'

def create_tts(text, name): #Gets text and name from run.py and creates a .mp4 file at a set folder
    filepath = os.path.join(baseFilepath, name)
    engine.save_to_file(text,filepath)
    engine.runAndWait()
    print("created tts file")

def create_tts_title(title,name):
    filepath = os.path.join(baseFilepath,name)
    engine.save_to_file(title,filepath)
    engine.runAndWait()
    print('Created tts title file')


if __name__ == '__main__':
    create_tts('This is a test .mp3 file. I am using multiplllle kinds of spech LMAO lol f*ck','test.mp3')
    create_tts_title('This is a test title','testTitle.mp3')
