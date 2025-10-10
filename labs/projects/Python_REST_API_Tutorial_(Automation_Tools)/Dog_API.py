# Shibe.Online API Example
import requests

api_url = "https://dog.ceo/api/breeds/image/random"

url_of_random_dog_image = dict(requests.get(api_url).json())["message"] #this is a string
# print(url_of_random_dog_image) #it returns an https image (we aren't pulling something as hackable)