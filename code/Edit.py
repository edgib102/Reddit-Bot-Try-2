from moviepy.editor import *
import os


#edits the image and mp3 file together to make a webm(for transparency), then stiches all the files into one and adds extra effects like background music into an mp4 

IMAGE_PATH = 'Video\\Image Bin\\'
TTS_PATH = 'Video\\Tts\\'
OUTPUT_PATH = 'Video\\Output\\'
BACKGROUND_PATH = 'Video\\Background\\'


def create_clip(amount):
    clips = []
    width = 1920/4
    height = 1080/4

    for x in range(amount):

        audioClip = AudioFileClip(TTS_PATH + f'testA{x}.mp3')
        commentClip = ImageClip(IMAGE_PATH + f'test{x}.png').set_duration(audioClip.duration + 0.5) #creates base clips
        tmp_mp4 = concatenate([commentClip], method='compose') #converts to files
        tmp_mp3 = CompositeAudioClip([audioClip])

        tmp_mp4.audio = tmp_mp3
        clips.append(tmp_mp4)

    stacked_vid = concatenate(clips, method='compose')
    stacked_vid = stacked_vid.resize((width,height))
    BackgroundClip = VideoFileClip(BACKGROUND_PATH + 'x.mp4').set_duration(stacked_vid.duration)
    BackgroundClip.set_position((width/2,height/2))    
    BackgroundClip = BackgroundClip.resize((width,height))
    

    final_vid = CompositeVideoClip([BackgroundClip,stacked_vid]) #clips_array([[BackgroundClip],[stacked_vid]])
    final_vid = final_vid.resize(width=width,height=height)
    final_vid.write_videofile(os.path.join(OUTPUT_PATH,'siming.mp4'),fps=10)

create_clip(1)
    

    

