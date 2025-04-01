import requests

API_URL = "https://my-json-server.typicode.com/WonterRobter/battle-cats-enemies/enemies"

def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        print("Battle Cats Enemies")
        for item in data:
            print(f"ID: {item['id']}, Naam: {item['name']}, Type: {item['type']}, Health: {item['health']}, Damage: {item['damage']}, Range: {item['range']}, Speed: {item['speed']}, Target: {item['target']}")
    else:
        print("❌ Fout bij ophalen van data")

fetch_data()
