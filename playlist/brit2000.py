from spotipy import Spotify

from playlist import auth_manager
from playlist import make_or_update_playlist
from playlist import Playlist


if __name__=="__main__":

    make_or_update_playlist(
        playlist=Playlist(
            _id="6UsMjYNDXqMAF44R5Pn3HY",
            name="Brit 2000",
            description="",
            artists=["strokes", "arctic monkeys", "kasabian"],
        )

    )