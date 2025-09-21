"""Make a PUT Request Webpage Notes
    -> PUT requests send information to the server, like POST requests do
    -> the user id also needs to be specified as a path variable to make put requests *to this API*
    -> APIs ARE A FORM OF WEB SERVICE
        -> MAKING CALLS TO THEIR ENDPOINTS
"""

#import modules
import requests

#store the url of the API we want to make the call to in a variable
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#what we want to send to the URL, THIS IS CONTAINED BY A DICTIONARY
body = {
    "first_name": "[YOUR UPDATED FIELD]",
    "last_name": "[YOUR UPDATED FIELD]",
    "email": "[YOUR EMAIL]"
}

#Executing the PUT request
    #this is done using the .put() method
response = requests.put(base_url + "/YOUR_ID", json=body) #the argument of this is the path to the url which we want to send the information contained in the dictionary we have just defined to
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url) #use the response module and the get method to execute the resquest
# print the data - see your updated record?
print(f"Response Content: {response.content}") #print out the request attribute from this

"""Video Notes 
    -> making a PUT request
    -> the resource ID is submitted in the request body 
    -> the API has since been updated to require the request parameter to be placed in the URL, stored in the variable at the beginning of the code, instead
    -> this means that the resource ID is now optional in the request body 
    -> using a PUT request to update an existing record
        -> updating the information which we previously added on the server
        -> he is using the requests.put() method
        -> WE ARE PASSING IN INFORMATION TO UPDATE
        -> this information is added into the dictionary (THIS IS THE REQUEST BODY)
        -> he makes one of the elements lowercase
        -> THE PUT REQUEST UPDATES THE INFORMATION WITH THE INFORMATION WE PLACE IN THE DICTIONARY 
"""