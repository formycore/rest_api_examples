import requests
import config

url = config.users()
#print(url)
r = requests.get(url)
#print(r)
#print(r.status_code)
#print(r.text)
#print(r.json())
print(r.content)