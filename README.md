# Spotify scripts

## Setup

To get client id and secret: https://developer.spotify.com/documentation/web-api/concepts/apps

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "SPOTIPY_CLIENT_ID=... \
SPOTIPY_CLIENT_SECRET=... \
SPOTIPY_REDIRECT_URI=..." > .env
```