import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
from datetime import date

VULFVERSE = dict(
    vulfpeck = "spotify:artist:7pXu47GoqSYRajmBCjxdD6",
    vulfmon = "spotify:artist:6pGuw52TrX5SZPdQSxAvgW",
    theo_katzman = "spotify:artist:2a4lU7F8toqKpb5v6Ftqya",
    woody_goss = "spotify:artist:11PSrxL3fUwegNhxdfP6zE",
    joey_dosik = "spotify:artist:3kANxNTLNOhxpOPoCbGq9E",
    antwaun_stanley = "spotify:artist:7vWFpgyWJ9CXisL0x6vYJN",
    cory_wong = "spotify:artist:6xt9sJmmyYwWkJv8A6ssiU",
    the_fearless_flyers = "spotify:artist:1JyLSGXC3aWzjY6ZdxvIXh",
    woody_and_jeremy = "spotify:artist:5P0unmRK5EI6psA51571i7"
)

PLAYLIST_NAME = "Vulfverse"
PLAYLIST_DESCRIPTION = "All the Vulfpeck universe"


load_dotenv()

auth_manager = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope='playlist-modify-public'
)
sp = spotipy.Spotify(auth_manager=auth_manager)

all_tracks: list[tuple[date, str]] = []

for artist_name, artist_id in VULFVERSE.items():
    res = sp.artist_albums(artist_id, album_type="album")
    albums = res["items"]
    while res["next"]:
        res = sp.next(res)
        albums.extend(res["items"])

    for album in albums:
        release_date = date.fromisoformat(album["release_date"])
        tracks = sp.album_tracks(album["id"])["items"]
        for track in tracks:
            all_tracks.append((release_date, track["id"]))

all_tracks.sort(key=lambda x: x[0])

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name=PLAYLIST_NAME,
    public=True,
    description=PLAYLIST_DESCRIPTION
)

# Add tracks to the playlist
track_ids = [track[1] for track in all_tracks]

# Spotify API allows adding a maximum of 100 tracks at a time
for i in range(0, len(track_ids), 100):
    sp.playlist_add_items(
        playlist_id=playlist["id"], items=track_ids[i:i + 100]
    )

print(f"Playlist '{PLAYLIST_NAME}' created successfully!")
