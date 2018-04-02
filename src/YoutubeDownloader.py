import os

#arg values
#1 -> link
#2 -> output_name
#3 -> switch (format)

def download(argv):

	audio_formats = ["mp3", "aac", "m4a", "flac"]
	video_formats = []
	
	argc = len(argv)
	if (argc < 1):
		print("Please provide a link!")
		return
	elif(argc > 3):
		print("Expected less arguments!")
		return

	call = "..\libs\youtube-dl"

	if(argc > 2):
		if(argv[2] in audio_formats):
			call += " --extract-audio --audio-format " + argv[2]

	call += " " + argv[0]

	if(argc > 1):
		call += " -o " + argv[1]

		
	print(call)
	os.system(call)