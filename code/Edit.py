from moviepy.editor import *
import os


#edits the image and mp3 file together to make a webm(for transparency), then stiches all the files into one and adds extra effects like background music into an mp4 

IMAGE_PATH = 'Video\\Image Bin\\'
TTS_PATH = 'Video\\Tts\\'
OUTPUT_PATH = 'Video\\Output\\'
EFFECT_PATH = 'Video\\Effects\\'

width = 1920/4
height = 1080/4

def create_clip(amount,audioNames,imageNames):
    clips = []
        
    titleaudioClip = AudioFileClip(TTS_PATH + 'TitleTtsAudio.mp3') #creates a one time title clip
    titleClip = ImageClip(IMAGE_PATH + 'TitleImage.png').set_duration(titleaudioClip.duration + 1.5)
    tmp_mp4 = concatenate([titleClip], method='compose')
    tmp_mp3 = CompositeAudioClip([titleaudioClip])

    tmp_mp4.audio = tmp_mp3
    clips.append(tmp_mp4)

    for x in range(amount):
        audioClip = AudioFileClip(TTS_PATH + audioNames[x])
        commentClip = ImageClip(IMAGE_PATH + imageNames[x]).set_duration(audioClip.duration + 1) #creates base clips
        tmp_mp4 = concatenate([commentClip], method='compose') #converts to files
        tmp_mp3 = CompositeAudioClip([audioClip])

        tmp_mp4.audio = tmp_mp3
        clips.append(tmp_mp4)

    stacked_vid = concatenate(clips, method='compose')
    stacked_vid = stacked_vid.resize((width,height))

    BackgroundClip = VideoFileClip(EFFECT_PATH + 'Background.mp4').set_duration(stacked_vid.duration)
    BackgroundClip.set_position((width/2,height/2))    
    BackgroundClip = BackgroundClip.resize((width,height))
    
    musicClip = AudioFileClip(EFFECT_PATH + 'Music.mp3').set_duration(stacked_vid.duration)
    musicClip2 = CompositeAudioClip([musicClip])
    BackgroundClip.audio = musicClip2

    final_vid = CompositeVideoClip([BackgroundClip,stacked_vid])
    final_vid = final_vid.resize(width=width,height=height)
    final_vid.write_videofile(os.path.join(OUTPUT_PATH,'siming.mp4'),fps=10)


if __name__ == '__main__':
    create_clip(1)
    

    

