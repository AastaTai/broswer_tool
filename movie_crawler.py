import urllib.request as req
import bs4

class movie_crawler:
    def __init__(self, url) -> None:
        self.NAME = []
        self.DATE = []
        self.URL = []
        self.url = url
        self.Request = req.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            },
        )
    
    def get_movie(self):
        with req.urlopen(self.Request) as response:
            self.data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(self.data, "html.parser")

        movie_list = root.find("ul", class_="movieList")
        movies = movie_list.find_all("section", class_="infoArea")
        # print(len(movies))

        n = 0
        for movie in movies:
            if n == 10:
                break
            print(movie)
            name = movie.find("h2").string
            date = movie.find("time").string
            url = movie.find("a")["href"]
            print(name)
            print(date)
            print(url)

            self.NAME.append(name)
            self.DATE.append(date)
            self.URL.append("https://www.vscinemas.com.tw/vsweb/film/" + url)
            n = n + 1
        
        return self.NAME, self.DATE, self.URL

if __name__ == "__main__":
    url = "https://www.vscinemas.com.tw/vsweb/film/index.aspx"
    movie = movie_crawler(url)
    movie.get_movie()