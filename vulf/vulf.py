import os
from dataclasses import dataclass
from dataclasses import field
from devtools import debug
from dotenv import load_dotenv
from datetime import date
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


# FIXME make this a yaml config file: `python playlist.py vulf.yml`
@dataclass
class Playlist:
    name: str
    description: str
    _id: str | None = None
    artists: list[str] = field(default_factory=list)


def get_artist_id_by_name(artist_name: str) -> str | None:
    
    results = sp.search(q='artist:' + artist_name, type='artist', limit=1)
    artists = results['artists']['items']
    
    if artists:
        return artists[0]['id']
    else:
        return None


def get_sorted_tracks(sp: Spotify, artist_ids: list[str]) -> list[str]:
    
    all_tracks: dict[str, date] = {}

    for artist_id in artist_ids:
        res = sp.artist_albums(artist_id)
        albums = res["items"]
        
        while res["next"]:
            res = sp.next(res)
            albums.extend(res["items"])

        for album in albums:
            try:
                release_date = date.fromisoformat(album["release_date"])
            except ValueError:
                release_date = date.fromisoformat(
                    f"{album['release_date']}-01-01"
                )
            tracks = sp.album_tracks(album["id"])["items"]
            for track in tracks:
                if artist_id in [
                    artist["uri"].split(":")[-1] for artist in track["artists"]
                ]:
                    all_tracks[track["id"]] = release_date
    # Sort the dictionary items by date
    all_tracks = sorted(all_tracks.items(), key=lambda item: item[1])
    track_ids = [track[0] for track in all_tracks]
    return track_ids


def remove_everything_from_playlist(
    sp: Spotify, user_id: str, playlist_id: str
) -> None:
    
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    track_uris = [item['track']['uri'] for item in tracks]
    
    for i in range(0, len(track_uris), 100):
        sp.user_playlist_remove_all_occurrences_of_tracks(
            user_id, playlist_id, track_uris[i:i+100]
        )


def make_or_update_playlist(sp: Spotify, playlist: Playlist):

    user_id = sp.current_user()["id"]

    artist_ids = [
        get_artist_id_by_name(artist_name=artist)
        for artist in playlist.artists
    ]
    track_ids = get_sorted_tracks(sp=sp, artist_ids=artist_ids)
    
    if playlist._id is not None:
        remove_everything_from_playlist(
            sp=sp, user_id=user_id, playlist_id=playlist._id
        )
    else:
        new_playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist.name,
            description=playlist.description,
            public=True,
            collaborative=False
        )

    for i in range(0, len(track_ids), 100):
        sp.playlist_add_items(
            playlist_id=playlist._id or new_playlist["id"],
            items=track_ids[i:i + 100]
        )

if __name__ == "__main__":
    
    load_dotenv()
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope='playlist-modify-public'
    )

    vulfverse = Playlist(
        _id="42pqYvkCmcUikeKd8TJMi9",
        name="Vulfverse",
        description="The whole Vulf pack.",
        artists=[
            "vulfpeck",
            "vulfpeck",
            "vulfmon",
            "theo katzman",
            "woody goss",
            "joey dosik",
            "antwaun stanley",
            "cory wong",
            "the fearless flyers",
            "woody and jeremy",
            "groove spoon",
            "my dear disco",
            "ella riot",
        ]
    )

    brit = Playlist(
        name="2000brit",
        description="Test playlist.",
        artists=["arctic monkeys", "the strokes"]
    )

    beatles = Playlist(
        name="The Beatles",
        description="John + George + Paul + Ringo",
        artists=[
            "beatles",
            "john lennon",
            "george harrison",
            "paul mccartney",
            "ringo starr"
        ]
    )

    sp = Spotify(auth_manager=auth_manager)

    make_or_update_playlist(sp=sp, playlist=beatles)