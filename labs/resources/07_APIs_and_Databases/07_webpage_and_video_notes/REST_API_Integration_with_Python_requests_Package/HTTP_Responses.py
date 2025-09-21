"""HTTP Responses
    -> when we make an API request, we get a response
    -> this is about the contents of the API response and the different information that it contains
    -> the content
        -> this contains the data
        -> the content is shown on the page
    -> the headers
        -> this contains information about the data that the API is returning
    -> other
        -> this can include the encoding, the URL and other pieces of information
"""

import requests #import the requests module

#the url which we want to make the API request to
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#use the get method to make a get request to the API
response = requests.get(base_url)

#print out the attributes of the API response object
print(f"Response Content: {response.content}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Encoding: {response.encoding}")
print(f"Response URL: {response.url}")

"""
    -> this is an http response object
    -> we are printing out the text of the response object 
    -> the headers give us information about what the response is made up of 
"""
