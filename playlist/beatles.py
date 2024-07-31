from _playlist import make_or_update_playlist
from _playlist import Playlist


if __name__=="__main__":
     
    make_or_update_playlist(
        playlist=Playlist(
            name="The Beatles",
            description="John + George + Paul + Ringo",
            artists=[
                "beatles",
                "john lennon",
                "george harrison",
                "paul mccartney",
                "ringo starr"
            ],
        )
    )