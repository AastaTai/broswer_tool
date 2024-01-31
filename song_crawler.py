import requests
import json

class song_crawler:
    def __init__(self, url) -> None:
        self.RANK = []
        self.SONG = []
        self.ARTIST = []
        self.URL = []
        self.url = url
    
    def get_song(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        song_list = data["data"]["charts"]["newrelease"]
        
        n = 0
        for song in song_list:
            if n == 10:
                break
            song_rank = song["rankings"]["this_period"]
            song_name = song["song_name"]
            song_url = song["song_url"]
            song_artist = song["artist_name"]
            
            print("排名:", song_rank)
            print("歌名:", song_name)
            print("連結:", song_url)
            print("作者:", song_artist)

            self.SONG.append(song_name)
            self.RANK.append(song_rank)
            self.URL.append(song_url)
            self.ARTIST.append(song_artist)
            n = n + 1
        return self.RANK, self.SONG, self.URL, self.ARTIST

if __name__ == "__main__":
    url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
    song = song_crawler(url)
    song.get_song()