import os
import sys
import spotipy
import spotipy.util as util

def getCredentials(filename):
	fin = open(filename).read()
	return fin.split("\n")

username, client_id, client_secret = getCredentials("credentials.sec")
redirect_uri = 'https://example.com/callback/'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(token)

print(sp.current_user_playing_track())