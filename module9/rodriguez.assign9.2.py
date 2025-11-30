import requests #gathering data from NASA fireball API
import json  # for formatting JSON

response = requests.get("https://ssd-api.jpl.nasa.gov/fireball.api?limit=20")
print(response.status_code  )  # Should print 200 if the request was successful
# JSON
data = response.json()

for fireball in data['data']: #printing date and energy of each fireball
    print(f"Date: {fireball[0]}, Energy: {fireball[1]}")


