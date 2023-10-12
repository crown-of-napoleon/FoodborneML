import requests

url = "https://api.foursquare.com/v3/places/search?ll=40.78%2C-73.97&radius=3000&categories=13000&fields=name%2Ctips"

headers = {
    "accept": "application/json",
    "Authorization": "fsq3Dl3iDc8CsQPIPhCegj1ofVGt+hDSvo1UXhM8QxkIYZg="
}

response = requests.get(url, headers=headers)

print(response.text)
