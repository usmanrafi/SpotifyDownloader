# import os
import pafy

def download(link, name, output):

	audio_formats = ["mp3", "aac", "m4a", "flac"]
	video_formats = ["mp4", "mkv"]

	video = pafy.new(link)

	dl = ""
	if(output in audio_formats):
		dl = video.getbestaudio()
	elif(output in video_formats):
		dl = video.getbestvideo()

	dlPath = "downloads/" + dl.title + "." + dl.extension
	dl.download(filepath=dlPath)

	# call = "..\libs\youtube-dl -f bestvideo+bestaudio"

	# if(output in audio_formats):
	# 	call += " --extract-audio --audio-format " + output

	# call += " " + link

	# call += " -o \"" + name + "\""
	# if(output in video_formats):
	# 	call += "." + output
	# if(output in audio_formats):
	# 	call += ".%(ext)s"
	
	# print(call)
	# os.system(call)
	
