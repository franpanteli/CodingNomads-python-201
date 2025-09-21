"""Working with JSON
    -> working with JSON response objects
    -> Python objects from JSON
        -> JSON is a format
        -> you can print out the content from this using Python methods
        -> PYTHON CAN BE USED TO CONVERT FROM JSON TO DICTIONARIES AND LISTS
    -> the JSON method
        -> the requests package has a JSON method
        -> the .json() method
        -> using the pprint package to pretty print data structures
"""

#import modules
import requests
from pprint import pprint

#define the base url which we are making the api get request to
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#use the get method in the requests package to make a get request to the url
    #this creates a dictionary
response = requests.get(base_url)

"""
    -> response is the response object from the http get request 
    -> we are then converting this into JSON, by using the .json() method 
    -> this prints the information from the http get request 
"""

data = response.json() #this converts the dictionary in the response object to a JSON object
# pprint(data)

#what happens if you print data['data'][0]['first_name']
#why is this?
print(data['data'][0]['first_name']) #Kendal
    #the result of this is Kendal, because we are extracting an element in the JSON object which was returned by the get request

"""
    -> json is a string 
    -> we can use the json method in the request package to convert this into a Python datatype 
    -> THE GET REQUEST ONLY RETURNS A STRING, SO WE ARE CONVERTING IT INTO A JSON SO THAT IT IS EASIER TO ACCESS ITS INFORMATION 
    -> IT CONVERTS IT INTO A JSON OBJECT, BUT IN REALITY THIS IS A DICTIONARY 
    -> we have data, error and status code 
    -> if we want to access the first item in the list, it's data['data'][0]['first_name'] 
        -> this prints the first name of the first user in the response body
"""