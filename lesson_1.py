
import requests
import json

url = 'https://api.github.com/repositories'
user = 'EVD11'

r = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(r.json(), f)