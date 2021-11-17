# Example that shows calling an external http rest API that returns json data
import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
json = response.json()
for person in json['people']:
    print(person['name'])