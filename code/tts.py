import pyttsx3
import os.path
engine = pyttsx3.init()
baseFilepath = 'Video\\Tts'

def create_tts(text, name): #Gets text and name from run.py and creates a .mp4 file at a set folder
    filepath = os.path.join(baseFilepath, name)
    engine.save_to_file(text,filepath)
    engine.runAndWait()

if __name__ == '__main__':
    create_tts('This is a test .mp3 file. I am using multiplllle kinds of spech LMAO lol f*ck','test.mp3')
