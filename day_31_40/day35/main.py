import requests
from twilio.rest import Client

account_sid = "AC98c76e83439bd564fc4f6533c4778b8f"
auth_token = "c7e2bba3240c51138c08cea8007b8c9c"


# twilio number: +17792235228

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "554736294b21e660660dd519362ea29d"


weather_params = {
    "lat": 41.00,
    "lon": 28.97,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(body="It's going to rain today. ",
            from_="",
            to=""
            )

print(message.status)
