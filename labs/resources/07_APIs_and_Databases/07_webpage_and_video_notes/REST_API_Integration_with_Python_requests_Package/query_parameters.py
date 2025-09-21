"""Query parameters
    -> a part of the URL or as a pair and argument
    -> like a WHERE clause for SQL
    -> THE QUERY PARAMETERS ARE KEY-VALUE PAIRS
        -> as a part of the URL
        -> ? IN THE URL INDICATES A QUERY PARAMETERS
        -> WE ARE ASKING THE SERVER FOR INFORMATION
        -> e.g http://demo.codingnomads.co:8080/tasks_api/tasks?userId=1&complete=true
            -> userID and complete
            -> THE QUERY PARAMETERS LIST STARTS WITH A ?, AND THE QUERY PARAMETERS ARE SEPARATED BY AN &
            -> THE RESPONSE OBJECT IN THIS EXAMPLE IS A JSON FILE, JAVASCRIPT OBJECT NOTATION
    -> QUERY PARAMETERS CAN BE PASSED INTO THE URL, OR AS A KEY-VALUE PAIR IN THE REQUEST
"""

import requests #import the requests module

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email=glillemani@bandcamp.com")
    #use the requests module and the get method
    #we are retrieving information from this api (with the link)

print(response.status_code) #print the status code of this request

# is the same as

params = { #store the parameters in a dictionary
    "email": "glillemani@bandcamp.com"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=params)
    #this is the same as using a get method on a shorter url, with everything as before the question mark

print(response.status_code)
"""
    -> they are key value pairs that exist in the url 
    -> you can print out the json response of the call 
    -> THE QUERY PARAMETERS CAN BE TAKEN OUT AND PUT IN A DICTIONARY 
    -> THIS DICTIONARY IS THEN PASSED AS THE SECOND ARGUMENT (FOR params) IN A GET REQUEST
"""