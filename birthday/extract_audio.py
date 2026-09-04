from moviepy import VideoFileClip
import os

video = VideoFileClip(os.path.join("birthday","memory.mp4"))
video.audio.write_audiofile(os.path.join("birthday","memory_music.mp3"))
video.close()

print("done") 