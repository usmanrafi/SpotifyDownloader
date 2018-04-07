import os

def download(link, name, output):

	audio_formats = ["mp3", "aac", "m4a", "flac"]
	video_formats = ["mp4", "mkv"]

	call = "..\libs\youtube-dl -f bestvideo+bestaudio"

	if(output in audio_formats):
		call += " --extract-audio --audio-format " + output

	call += " " + link

	call += " -o \"" + name + "\""
	if(output in video_formats):
		call += "." + output
	if(output in audio_formats):
		call += ".%(ext)s"
	
	print(call)
	os.system(call)
