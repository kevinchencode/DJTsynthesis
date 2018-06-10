from moviepy.editor import *
import os

list = os.listdir(".")
list = [x for x in list if x[-4:] == ".mp4"]
for vid in list:
	video_clip = VideoFileClip(vid)
	audio_clip = video_clip.audio
	audio_clip.write_audiofile(vid.split(".mp4")[0] + ".mp3")
