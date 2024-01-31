from flask import Flask, render_template
from weather import weather
from news_crawler import news_crawler
from song_crawler import song_crawler
from movie_crawler import movie_crawler
from currency import currency
from datetime import datetime


app = Flask(__name__, template_folder='C:\\git\\data\\final_database\\templates')

users = ["vivi", "loretta"]

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', users=users)

@app.route('/<username>')
def user(username):
    if username == "vivi":
        current_date = datetime.now().strftime("%A, %B %d, %Y")

        url = "https://tw.news.yahoo.com/"
        Crawler = news_crawler(url)
        URL, TITLE = Crawler.get_news()
        news_data1 = zip(URL, TITLE)

        url = "https://tw.news.yahoo.com/entertainment/"
        Crawler = news_crawler(url)
        URL, TITLE = Crawler.get_news()
        news_data2 = zip(URL, TITLE)

        Weather = weather("桃園市")
        WX, POP, MINT, MAXT, CI = Weather.get_weather()

        url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
        Song = song_crawler(url)
        RANK, SONG, URL, ARTIST = Song.get_song()
        song_data = zip(RANK, SONG, URL, ARTIST)

        return render_template(str(username)+'.html', username=username, current_date=current_date, news_data1=news_data1, news_data2=news_data2, WX=WX, POP=POP, MINT=MINT, MAXT=MAXT, CI=CI, song_data=song_data)
    elif username == "loretta":
        current_date = datetime.now().strftime("%A, %B %d, %Y")

        url = "https://tw.news.yahoo.com/"
        Crawler = news_crawler(url)
        URL, TITLE = Crawler.get_news()
        news_data1 = zip(URL, TITLE)

        url = "https://tw.news.yahoo.com/world/"
        Crawler = news_crawler(url)
        URL, TITLE = Crawler.get_news()
        news_data2 = zip(URL, TITLE)

        url = "https://tw.news.yahoo.com/finance/"
        Crawler = news_crawler(url)
        URL, TITLE = Crawler.get_news()
        news_data3 = zip(URL, TITLE)

        Weather = weather("桃園市")
        WX, POP, MINT, MAXT, CI = Weather.get_weather()

        currency_ = currency()
        Currency, Buying, Selling = currency_.get_currency()
        currency_data = zip(Currency, Buying, Selling)

        url = "https://www.vscinemas.com.tw/vsweb/film/index.aspx"
        movie = movie_crawler(url)
        movie.get_movie()
        movie_data = zip(movie.NAME, movie.DATE, movie.URL)

        return render_template(str(username)+'.html', username=username, current_date=current_date, news_data1=news_data1, news_data2=news_data2, news_data3=news_data3, WX=WX, POP=POP, MINT=MINT, MAXT=MAXT, CI=CI, currency_data=currency_data, movie_data=movie_data)
        

if __name__ == '__main__':
    app.debug = True
    app.run(port= 5555)