"""Make a POST Request Webpage Notes
    -> POST requests can send data to the server
    -> THIS IS DONE BY USING THE .post() METHOD
    -> to pass information into the POST request, we use the JSON parameter
"""

import requests #import the requests module

#store the url we want to make the api request from in another variable
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#STORE THE DATA WE WANT TO POST TO THE API ENDPOINT IN A DICTIONARY, WITH KEY-VALUE PAIRS
body = {
    "first_name": "[YOUR FIRST NAME FIELD]",#add first name inside quotes
    "last_name": "[YOUR LAST NAME FIELD]",#add last name inside quotes
    "email": "[YOUR EMAIL FIELD]"#add email inside quotes
}

#use the .post() method to send the information stored in the base_url dictionary to the API
response = requests.post(base_url, json=body)

"""Video Notes
    -> making post requests with the post() method 
    -> TO SEND INFORMATION AND CREATE A RECORD
    -> WE USE A DICTIONARY FOR THIS 
    -> this is named body 
    -> we fill the dictionary with the record we want to create 
    -> we are passing this information in as a parameter
    -> the user we are adding isn't already in the database
    -> after checking this, the user has been added
"""
