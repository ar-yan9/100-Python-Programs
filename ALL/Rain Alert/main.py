import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7f51c1e482c3930555313d46debeb0a7"

MY_LAT = 28.6139  # New Delhi, India
MY_LONG = 77.2090

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella! ☂️")
else:
    print("No rain today! ☀️")