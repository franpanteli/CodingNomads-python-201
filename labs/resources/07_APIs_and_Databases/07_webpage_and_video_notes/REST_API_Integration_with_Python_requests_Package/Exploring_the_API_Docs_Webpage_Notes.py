"""Exploring the API Docs Webpage Notes
    -> we have seen GET, POST, PUT and DELETE requests with the requests package
    -> all the examples so far only use the user's endpoint
    -> we want to look at the API documentation and explore it
        -> creating new tasks and users
        -> updating existing records
        -> removing records
    -> this is the documentation URL: http://demo.codingnomads.co:8080/tasks_api/swagger-ui/index.html#/
        -> the documentation is only for the API which was used in the course examples
        -> the API provides public records
            -> these are read with GET requests
            -> you can add extra records, which aren't visible to other users
            -> the changes to the data the API stores are updated daily
    -> in the API documentation
        -> creating new tasks and users
        -> updating existing records
        -> removing records
    -> the documentation contains examples of code that we can use to interact with the API
"""

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
  "data": [
    {
      "id": 0,
      "userId": 0,
      "name": "string",
      "description": "string",
      "createdAt": "2025-09-21T18:54:37.408Z",
      "updatedAt": "2025-09-21T18:54:37.408Z",
      "completed": false
    }
  ],
  "error": {
    "message": "string"
  },
  "status": "string"
}

# here we execute the PUT request
response = requests.put(base_url + "/YOUR_ID", json=body)
# print the status code (hopefully it's 200 which means all is well)
print(f"Response Code: {response.status_code}")

# let's make a GET request to retrieve the new data from the server
response = requests.get(base_url)
# print the data - see your updated record?
print(f"Response Content: {response.content}")
