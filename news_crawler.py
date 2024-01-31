import urllib.request as req
import bs4
import pandas as pd

class news_crawler:
    def __init__(self, url) -> None:
        self.URL = []
        self.TITLE = []
        self.CONTENT = []
        self.url = url
        self.Request = req.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            },
        )
        self.df = pd.DataFrame()

    def get_news(self):
        with req.urlopen(self.Request) as response:
            self.data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(self.data, "html.parser")

        titles = root.find_all("ul", class_="H(100%) D(ib) Mstart(24px) W(32.7%)")

        title = titles[0].find_all("li", class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")

        for article in title:
            if article.a.string != None:
                link = article.a["href"]
                url = self.url + link
                self.URL.append(url)
                Request = req.Request(
                    url,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    },
                )
                with req.urlopen(Request) as response:
                    data1 = response.read().decode("utf-8")

                branch = bs4.BeautifulSoup(data1, "html.parser")
                t = branch.find("div", class_="caas-title-wrapper")
                print(t.string)
                self.TITLE.append(t.string)

                # contents = branch.find("div", class_="caas-body")
                # c = contents.find_all("p")
                # text = ""
                # for i in c:
                #     if i.string != None:
                #         print(i.string)
                #         text += i.string
                
                # self.CONTENT.append(text)
        self.df["URL"] = self.URL
        self.df["TITLE"] = self.TITLE
        # self.df["CONTENT"] = self.CONTENT

        file_name = 'final_database/yahooNews.xlsx'
        self.df.to_excel(file_name)

        return self.URL, self.TITLE

if __name__ == "__main__":
    # url = "https://tw.news.yahoo.com/"
    # url = "https://tw.news.yahoo.com/world/"
    url = "https://tw.news.yahoo.com/entertainment/"
    crawler = news_crawler(url)
    crawler.get_news()