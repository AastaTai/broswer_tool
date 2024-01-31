import pandas as pd

class currency():
    def __init__(self) -> None:
        self.currency = []
        self.SpotRate_buying = []
        self.SpotRate_selling = []

    def get_currency(self):
        dfs = pd.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
        currency = dfs[0]
        # print(currency)

        currency = currency.iloc[:, 0:5]
        currency.columns = ["幣別", "現金匯率(買入)", "現金匯率(賣出)", "即期匯率(買入)", "即期匯率(賣出)"]
        currency["幣別"] = currency["幣別"].str.extract("\((\w+)\)")
        print(currency)
        for i in range(len(currency)):
            if currency.iloc[i, 0] in "USDSEKEUR":
                self.currency.append(currency.iloc[i, 0])
                self.SpotRate_buying.append(currency.iloc[i, 3])
                self.SpotRate_selling.append(currency.iloc[i, 4])
        return self.currency, self.SpotRate_buying, self.SpotRate_selling

if __name__ == "__main__":
    currency = currency()
    Currency, Buying, Selling = currency.get_currency()
    print(Currency, Buying, Selling)