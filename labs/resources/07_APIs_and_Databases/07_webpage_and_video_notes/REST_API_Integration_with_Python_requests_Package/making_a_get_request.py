"""
    -> for getting data from the server
    -> this is a RESTful request
    -> [http://demo.codingnomads.co:8080/tasks_api/users] <- THIS IS AN ENDPOINT
    -> install a json formatter for the browser
    -> import requests, then use a get request to print out the status code of the response
    -> if the base url is changed, then this should return a 404 status code (error)
        -> THE API DOES NOT HAVE THIS ENDPOINT
    -> REST is a standard form of API communication
        -> REpresentational State Transfer
        -> for client and server communication
    -> we are making a GET request to an API endpoint
"""

import requests
url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url) #GET IS AN HTTP METHOD, this is a response object
print(response.status_code) #200 means it is successful
