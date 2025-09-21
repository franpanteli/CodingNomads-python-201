"""Rest API Integration with Python Requests Package Webpage Notes
    -> outline
        -> intro to APIs with Python
        -> requests package / queries
        -> GET requests
        -> JSON Python objects
        -> making a POST / PUT / DELETE request
        -> API docs
        -> REST API integration with Python

    -> into to APIs with Python
        -> APIs
        -> web services
        -> interacting with the network of APIs
        -> RESTful API requests and responses
        -> requests IS A PYTHON MODULE
"""
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
request = requests.get(base_url)

"""
    -> requests package
    -> create a new project with a new virtual environment 
    -> to send http compliant requests with Python 
    -> to access response data and work with returned information 
    -> making http requests with Python
    -> HE INSTALLS THE requests PACKAGE IN A VIRTUAL ENVIRONMENT 
"""
