import os
import requests
import config
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("TOKEN")
print("api_key:", api_key )

#print(config.users())

# r = requests.get(config.users())

# print(r.json())