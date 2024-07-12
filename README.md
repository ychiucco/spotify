# Spotify scripts

## Setup
```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ echo 'SPOTIPY_CLIENT_ID=...
SPOTIPY_CLIENT_SECRET=...
SPOTIPY_REDIRECT_URI=...' > .env
```

## `Vulfverse` playlist

Create a playlist with all the songs of the Vulfpeck universe:
everything that has a Vulfpeck artist playing.

```sh
$ python vulf/vulf.py

Playlist 'Vulfverse' created successfully with a total of 862 songs!
```

