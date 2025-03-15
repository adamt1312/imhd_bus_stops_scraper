import requests
import json
from bs4 import BeautifulSoup
import time

# 🚀 Constants
BASE_URL = "https://imhd.sk/ba/online-zastavkova-tabula?st={}"
OUTPUT_FILE = "bus_stops2.json"
MAX_STATION_ID = 584

def get_stop_name(station_id):
    url = BASE_URL.format(station_id)
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    stop_name_element = soup.find(id="stop-name")

    return stop_name_element.text.strip() if stop_name_element else None

def scrape_bus_stops():
    bus_stops = []
    station_id = 1  # Start at ID 1

    while station_id <= MAX_STATION_ID:
        stop_name = get_stop_name(station_id)

        if stop_name:
            bus_stops.append({"id": station_id, "stop_name": stop_name})
            print(f"✅ Found: {stop_name} (ID: {station_id})")
        else:
            print(f"⚠️ No stop found for ID: {station_id}")

        station_id += 1
        time.sleep(0.3)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bus_stops, f, ensure_ascii=False, indent=4)
    
    print(f"\n🚀 Done! {len(bus_stops)} stops saved to `{OUTPUT_FILE}`.")

if __name__ == "__main__":
    scrape_bus_stops()
