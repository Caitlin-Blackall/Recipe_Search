import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ask the user to enter a cuisine type
cuisine_type = input("Enter a cuisine type to search for: ")

# Use the Spotify API to search for playlists related to the cuisine type - need to add client_id and client_secret
client_credentials_manager = SpotifyClientCredentials(client_id='enter your id here', client_secret='enter your secret/key here')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.search(q=cuisine_type, type='playlist')

# Display the playlists for each search result
playlists = results['playlists']['items']
for playlist in playlists:
    print(playlist['name'])
    print(playlist['external_urls']['spotify'])
    print()