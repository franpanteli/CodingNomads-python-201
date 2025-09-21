"""Make a DELETE Request Webpage Notes
    -> the DELETE request can send information to the API
    -> it does not contain information
    -> in this example, the server is sent a URL to the path of the user which we wnat to delete
"""

#import modules
import requests

#the url of the API we want to make the delete request to
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#using the .delete() method in the requests module
    #the argument of this is the relative path of the data which we want to delete on the API
response = requests.delete(base_url + "/50")

    #using the .status_code attribute to print out the API data without the result we just deleted
print(response.status_code) #500

"""Video notes 
    -> making a delete request
    -> DELETE is an http method to remove records and delete information 
    -> we aren't sending it data
    -> he is changing the code from the previous example
    -> we are then changing the path variable with the data we want to delete
        -> deleting Kim as a user (in this example)
    -> this can be checked by refreshing the API to see if the delete has been made 
    -> this is the end of the http methods using the requests package 
"""

