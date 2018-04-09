import urllib.request as req

import YoutubeDownloader as ytdl

def dl(link, name, output):
	ytdl.download(link, name , output)


def searchAndDl(name, output="mp3"):

	url = "https://www.youtube.com/results?search_query="
	query = name.split(' ')
	for word in query:
		url += word + "+"
	url = url[:-1]	# removing the last +

	src = req.urlopen(url).read()
	src = str(src)

	#acquiring the first link
	vid = src[src.find("/watch?v="):]
	vid = vid[:vid.find("\"")]
		
	link = 'https://www.youtube.com' + vid 

	print(link)
	dl(link, name, output)