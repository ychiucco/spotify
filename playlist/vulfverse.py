from _playlist import make_or_update_playlist
from _playlist import Playlist


if __name__=="__main__":

    make_or_update_playlist(
        playlist=Playlist(
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
            ],
        )
    )