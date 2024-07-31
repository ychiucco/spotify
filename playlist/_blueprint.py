from _playlist import make_or_update_playlist
from _playlist import Playlist


if __name__=="__main__":

    make_or_update_playlist(
        playlist=Playlist(
            _id=None,
            name="",
            description="",
            artists=[],
        )

    )