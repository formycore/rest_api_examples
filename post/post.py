import requests
import config
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("TOKEN")

url = config.users()
name = input ("Enter the name: ")
email = input("Enter the email : ")
status = input("Enter the status :")
gender = input("Enter the gender: ")

data = dict()
data['name'] = name
data['email'] = email
data['status'] = status
data['gender'] = gender

print(data)