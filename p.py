import requests
import os
from pprint import pprint

#https://api.restful-api.dev/objects

def getData():
  id = input("Enter data id : ")
  # url = f"{os.getenv("API_URL")}/objects"
  url =f"https://api.restful-api.dev/objects/{id}"
  data = requests.get(url)
  pprint(data.json())


if __name__ == "__main__" :
  getData()