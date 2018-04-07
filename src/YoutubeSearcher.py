import bs4
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

	src = req.urlopen(url)
	soup = bs4.BeautifulSoup(src, 'lxml')

	vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
		
	link = 'https://www.youtube.com' + vid['href']
	dl(link, name, output)