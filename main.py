import requests 
import os 
from twilio.rest import Client


weather_api_key = os.environ.get("OWP_API_KEY")
account_sid = "AC7fabf305dbb69aaa81ef45635f18aefb"
auth_token = os.environ.get("AUTH_TOKEN")

# to run the application locally sign into open weather and get an api key. Do the same with twilio and get the auth_token

parameters = {
    "lat": 43.073051, 
    "lon": -89.401230,
    "appid": weather_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_be_sunny = False 
will_rain = False
will_be_stormy = False 
is_cloudy = False 

for _ in range(0, 12, 1):
    hourly_weather_id = data["hourly"][_]["weather"][0]["id"]
    if 300 <= int(hourly_weather_id) <= 700:
        will_rain = True 
    elif int(hourly_weather_id) == 800:
        will_be_sunny = True
    elif 200 <= int(hourly_weather_id) < 300:
        will_be_stormy = True
    elif int(hourly_weather_id) > 800:
        is_cloudy  = True 

# or use the slice function for simplicity 
# hourly_rain_id = data["hourly"][0]["weather"][0]["id"]


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It is going to rain today. Remember to bring your umbrella ☂️",
                     from_='+13642047422',
                     to='+919819147217'
                 )
    print(message.status)

if will_be_sunny:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It is going to be sunny ☀️ Go take a walk :)",
                     from_='+13642047422',
                     to='+919819147217'
                 )
    print(message.status)

if will_be_stormy:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It is going to be stormy⚡- Please stay inside!",
                     from_='+13642047422',
                     to='+919819147217'
                 )


    print(message.status)

if is_cloudy:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It is going to be cloudy today ☁️, time to chill in the library ",
                     from_='+13642047422',
                     to='+919819147217'
                 )


    print(message.status)
    # can also alternatively print the message.sid -> to check if an id was generated for the message 
    
