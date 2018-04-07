import os
import sys
import json

import spotipy
import spotipy.util as util

import YoutubeSearcher as yt

def getCredentials(filename):
	fin = open(filename).read()
	return fin.split("\n")

username, client_id, client_secret = getCredentials("credentials.sec")
redirect_uri = 'https://example.com/callback/'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(token)

resp = json.loads(json.dumps(sp.current_user_playing_track()))
details = resp["item"]

album_name = details["album"]["name"] 
song_name = details["name"]
artists_name = details["artists"][0]["name"]

print(song_name)
print(artists_name)

yt.searchAndDl(artists_name + " " + song_name, "mp3")