import requests
import pandas as pd

class weather():
    def __init__(self, location) -> None:
        self.authorization = "CWA-6FF8E932-754A-4AF8-87F3-06B51BC78ABB"
        self.url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
        self.location = location
        self.wx = ""
        self.pop = ""
        self.mint = ""
        self.maxt = ""
        self.ci = ""
    
    def get_weather(self):
        res = requests.get(self.url, {"Authorization": self.authorization})
        self.resJson = res.json()

        # process resJson to get the data by for loop
        for data in self.resJson["records"]["location"]:
            if data["locationName"] == "桃園市":
                print(data["locationName"])
                for weather in data["weatherElement"]:
                    if weather["elementName"] == "Wx":
                        self.wx = weather["time"][0]["parameter"]["parameterName"]
                        print("天氣現象", weather["time"][0]["parameter"]["parameterName"])
                    if weather["elementName"] == "PoP":
                        self.pop = weather["time"][0]["parameter"]["parameterName"]
                        print("降雨機率", weather["time"][0]["parameter"]["parameterName"])
                    if weather["elementName"] == "MinT":
                        self.mint = weather["time"][0]["parameter"]["parameterName"]
                        print("最低溫", weather["time"][0]["parameter"]["parameterName"])
                    if weather["elementName"] == "MaxT":
                        self.maxt = weather["time"][0]["parameter"]["parameterName"]
                        print("最高溫", weather["time"][0]["parameter"]["parameterName"])
                    if weather["elementName"] == "CI":
                        self.ci = weather["time"][0]["parameter"]["parameterName"]
                        print("舒適度", weather["time"][0]["parameter"]["parameterName"])

        return self.wx, self.pop, self.mint, self.maxt, self.ci
                    

if __name__ == "__main__":
    weather = weather("桃園市")
    weather.get_weather()