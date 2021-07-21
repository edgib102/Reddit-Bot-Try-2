
from moviepy.editor import *
import os


#edits the image and mp3 file together to make a webm(for transparency), then stiches all the files into one and adds extra effects like background music into an mp4 

IMAGE_PATH = 'Video\\Image Bin\\'
TTS_PATH = 'Video\\Tts\\'
OUTPUT_PATH = 'Video\\Output\\'


def create_clip(amount):
    clips = []

    for x in range(amount):

        audioClip = AudioFileClip(TTS_PATH + f'testA{x}.mp3')
        commentClip = ImageClip(IMAGE_PATH + f'test{x}.png').set_duration(audioClip.duration + 0.5) #creates base clips

        tmp_mp4 = concatenate([commentClip], method='compose') #converts to files
        tmp_mp3 = CompositeAudioClip([audioClip])

        tmp_mp4.audio = tmp_mp3
        clips.append(tmp_mp4)
        
    final_vid = concatenate(clips, method='compose')

    final_vid.write_videofile(os.path.join(OUTPUT_PATH,'siming.mp4'),
        fps=10,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True
    )

create_clip(5)
    

    

