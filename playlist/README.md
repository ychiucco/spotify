# Playlist

This module is used to create new playlists or update existing ones.

It needs the main `venv` active.

- copy `_blueprint.py` into a new file in this folder:
```console
cp _blueprint.py my_playlist.py
```
- fill the `Playlist` object inside the new file with the desired attributes of the playlist:
    - `name`,
    - `description`,
    - `artists`;
- if you want to update an existing playlist, also provide the `_id`;
- execute the new file as a script:
```console
python my_playlist.py
```
- if you are creating a new playlist, its `_id` is returned at the end of the procedure: copy it and paste it in your file to keep updating the same playlist in the future (or get it directly from the Spotify page).