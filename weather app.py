import requests
city=input("Enter city name:")
url=f"https://wttr.in/{city}?format=j1"
response= requests.get(url)
data=response.json()
temp=data["current condition"][0]["temp_C"]
weather= data["current condition"][0]["weatherDesc"][0]["value"]
print("Temperature",temp,"*C")
print("Weather:",weather)