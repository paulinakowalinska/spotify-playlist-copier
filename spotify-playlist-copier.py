import json
import requests
from secrets import spotify_user_id, spotify_token, spotify_playlist_id, client_secret, client_id, number_of_tracks


class CopyPlaylist:

    def __init__(self):
        self.token = spotify_token
        self.user_id = spotify_user_id
        self.playlistid = spotify_playlist_id
        self.clientsecret = client_secret
        self.clientid = client_id
        self.number_of_tracks = number_of_tracks

    def get_playlist(self):
        artists = []
        songs = []

        query = f"https://api.spotify.com/v1/playlists/{self.playlistid}/tracks"
        response = requests.get(query,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {self.token}"})
        json_response = response.json()

        for i in range(0, self.number_of_tracks):
             artists.append(json_response['items'][i]['track']['artists'][0]['name'])
             songs.append(json_response['items'][i]['track']['name'])
        return artists, songs

    def get_playlist_name(self):
        query = f"https://api.spotify.com/v1/playlists/{self.playlistid}"
        response = requests.get(query,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {self.token}"})
        json_response = response.json()
        return json_response['name']

    def get_song_id(self, name, artist):
        track_name = name
        artist_name = artist
        query = f"https://api.spotify.com/v1/search?q=track%3A{track_name}%20artist%3A{artist_name}&type=track"
        response = requests.get(query,
                        headers = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {self.token}"})
        json_response = response.json()
        try:
            id = json_response['tracks']['items'][0]['uri']
        except IndexError:
            id = ''
        return id

    def create_copy(self, name):
        request_body = json.dumps({
            "name": name,
            "description": "This is a copied playlist.",
            "public": False
        })

        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(
            query,
            data = request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization": f"Bearer {self.token}"
            }
        )
        json_response = response.json()
        id = json_response['id']
        return id

    def fill_playlist(self, myplaylist_id, song_ids):
        query = f"https://api.spotify.com/v1/playlists/{myplaylist_id}/tracks"
        request_body = json.dumps({
            "uris": song_ids
        })
        response = requests.post(
            query,
            data = request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization": f"Bearer {self.token}"
            }
        )
        json_response = response.json()
        print(json_response)

if __name__ == '__main__':
    cp = CopyPlaylist()
    artists, songs = cp.get_playlist()
    name = cp.get_playlist_name()
    my_playlist_id = cp.create_copy(name)
    id=[]
    for i in range(0, number_of_tracks):
       id.append(cp.get_song_id(songs[i], artists[i]))
    id_new = list(filter(None, id))
    cp.fill_playlist(my_playlist_id, id_new)
