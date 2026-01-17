import requests

latitude = 50.45
longitude = 30.24

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)

data["latitude"]
data["current"]["time"]

def get_temperature(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    print(data["current"]["temperature_2m"])

get_temperature(48.5, 75.34)
get_temperature(-83.5, 5.34)
get_temperature(2.5, 37.34)
