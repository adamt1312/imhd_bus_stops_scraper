import requests
import json
from bs4 import BeautifulSoup


def getStopName(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find(id="stop-name").text
    except:
        return "NaN"

if __name__ == '__main__':
    stopNumNameArr = []
    for x in range(580):
        stop_name = getStopName(f"https://imhd.sk/ba/online-zastavkova-tabula?st={x + 1}")
        print(x + 1, stop_name)
        stopNumNameArr.append({"id": x + 1, "stop_name": stop_name})

    with open("bus_stops.json", "w", encoding='utf8') as jsonFile:
        json.dump(stopNumNameArr, jsonFile, ensure_ascii=False)
