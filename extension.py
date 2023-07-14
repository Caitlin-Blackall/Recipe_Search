import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ask the user to enter a cuisine type
cuisine_type = input("Enter a cuisine type to search for: ")

# Use the Spotify API to search for playlists related to the cuisine type
client_credentials_manager = SpotifyClientCredentials(client_id='01b9516fd1224b83b1c4362ba4b15b2e', client_secret='97375c132b5f4bcb98f379b11ccc5878')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.search(q=cuisine_type, type='playlist')

# Display the playlists for each search result
playlists = results['playlists']['items']
for playlist in playlists:
    print(playlist['name'])
    print(playlist['external_urls']['spotify'])
    print()