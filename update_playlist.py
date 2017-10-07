import pprint
import sys

import spotipy
import spotipy.util as util

import scrape

USERNAME = 'armunch'
PLAYLIST_ID = '4YCcVzEGE57NX4X1m7aUIv'

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(USERNAME, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_replace_tracks(USERNAME, PLAYLIST_ID, scrape.generate_tracklist())
    print(results)
else:
    print("Can't get token for", username)

