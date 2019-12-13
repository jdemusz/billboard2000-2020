import requests
import json

song_name = "Circles"
song_artist = "Post Malone"
song_year = "2019"
access_token = "BQDS3swBLa7G7hYL7FIwRiR188MnH8Uwkp5A3_D3rKgJ7DPkBhxTsSd-yfrx4d1_XBIejnkWnJrNjtnH-9C_lQcRjyElSasdtEMS2C4N0_GViBYAgYxZjOlyor8ifi8F5Ada10NW2fa3JnEKs-W8"

search_url = ("https://api.spotify.com/v1/search?q={0}%20artist:{1}%20year:{2}&type=track&market=US&include_external=audio").format(song_name, song_artist, song_year)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + access_token
}

song_response=requests.get(search_url, headers=headers).json()
print(json.dumps(song_response, indent=4))



