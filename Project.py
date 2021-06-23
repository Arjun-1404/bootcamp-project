import requests

from datetime import datetime
print("-----------------------------------")
print("Welcome to the Weather checker !!!")
print("-----------------------------------")
loc = input("Which City's weather you want to see : ")


total_link = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=3d075cc7a42957213d8f2ee6fab691e4"
api_link = requests.get(total_link)
data = api_link.json()

date_time = datetime.now().strftime("%d %b %y")
date_time1 = datetime.now().strftime("%I:%M:%S:%p")
temp = int((data["main"]["temp"]) - 273.15)
weather = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
wnd_spd = data["wind"]["speed"]


print("==================================================================")
print("Thw WEATHER for ", loc.upper(), "on", date_time, "at", date_time1, "is as follows :")
print("==================================================================")
print("The Current Temperature in", loc.upper(), "is : ", temp, "°C")

print("The Current Weather in", loc.upper(), "is : ", weather.upper())

print("The Current Humidity in", loc.upper(), "is : ", humidity)

print("The Current Wind Speed in", loc.upper(), "is : ", wnd_spd, " km/hr")
print("Thank You , Do Visit Again")
print("---------------------------------------------------------------------")
