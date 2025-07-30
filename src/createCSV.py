import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests as requests
import time

client_credentials_manager = SpotifyClientCredentials(client_id='input ID',
                                                      client_secret='input secret')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example function to fetch song data
def fetch_song_data(artist_name):
    client_credentials_manager = SpotifyClientCredentials(client_id='input ID',
                                                      client_secret='input Secret')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q=f'artist:{artist_name}', limit=30)  # Search for songs by artist
    songs = results['tracks']['items']
    track = results['tracks']['items'][0]
    artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
    time.sleep(30)

    song_data = []
    for song in songs:
        song_id = song['id']
        features = sp.audio_features(tracks=[song_id])
        time.sleep(10)
        song_info = {
            'Song': song['name'],
            'Artist': ', '.join([artist['name'] for artist in song['artists']]),
            'Year': song['album']['release_date'][0:4],
            'Genres': artist['genres'],
            'Acousticness': features[0]['acousticness'],
            'Danceability': features[0]['danceability'],
            'Duration': features[0]['duration_ms'],
            'Energy': features[0]['energy'],
            'Instrumentalness': features[0]['instrumentalness'],
            'Key': features[0]['key'],
            'Liveness': features[0]['liveness'],
            'Loudness': features[0]['loudness'],
            'Mode': features[0]['mode'],
            'Speechiness': features[0]['speechiness'],
            'Tempo': features[0]['tempo'],
            'Time Signature': features[0]['time_signature'],
            'Split': 'test'
        }
        song_data.append(song_info)

    return pd.DataFrame(song_data)

artist_lst = ['Teddy Swims', 'Johnny Cash', 'Frank Sinatra']
for artist in artist_lst:
    # Example usage
    print(artist)
    artist_name = artist  # Example artist
    song_df = fetch_song_data(artist_name)

    # Save DataFrame to CSV
    song_df.to_csv('SongCSV.csv', mode='a', index=False)

# Read the CSV file into a DataFrame
df = pd.read_csv('SongCSV.csv')
print(df)
