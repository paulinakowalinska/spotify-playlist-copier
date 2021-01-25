# spotify-playlist-copier
Python script to copy any Spotify playlist.

This script does the following:
- finds the names of the tracks and the artists on the playlist
- creates an empty playlist on the user's account
- fills it with the tracks from the other playlist

The copied playlist is private by default.

#### Here's what's needed to run this script:

- <a href="https://requests.readthedocs.io/en/master/">requests library</a>
- a Spotify Oauth `spotify_token` from the Spotify console
- `client_id`, `client_secret` from Spotify API
- `spotify_user_id` which is the username of the developer's Spotify
- `spotify_playlist_id` which is the URI of the Spotify playlist to be copied
- `number_of_tracks` in said playlist

Inspired by <a href="https://www.youtube.com/watch?v=7J_qcttfnJA&t=294s">this</a> video. 
