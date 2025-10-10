"""We are following the tutorial at: https://www.youtube.com/watch?v=4WNMMOk958A
    -> pseudocode
        -> make a venv, install requests
        -> get the tools for doing web requests
        -> an image API http://shibe.online/api/shibes
        -> a quotes API http://quotes.stormconsultancy.co.uk/random.json
        -> inspect those API
        -> get image and quote
        -> create a new file
        -> create HTML structure
        -> write to the file
    -> we create a virtual environment called venv for the project, and then install the requests module into this
        -> pip install requests <- this fetches the package from pypi (Python package index)
        -> be careful with what you pip install, because there are no security checks
            -> only install packages you know are safe
        -> API stands for application programming interface
            -> we can do multiple things with this programatically
            -> we can make programs interact with each other
            -> we can pull information from two or more APIs and combine them in one applicaiton, for example
            -> there are APIs for multiple purposes
                -> we can repurpose this and create different things from it
            -> each API has documentation
                -> for example, that we can make different get requests
                    -> with the Shibe API, we can generate random dog images, any given number of them between 1 and 100
                    -> this is an http get request and it returns a JSON object
                        -> JAVASCRIPT OBJECT NOTATION
                            -> it is like a list, or a dictionary
                            -> it can also be a list of dictionaries
                            -> we are using the Dog_API, not the Shibe API
                                -> it can be called any number of times
"""

# -> make a venv, install requests
# -> get the tools for doing web requests
import requests
import json #json is a module, JavaScript Object Notation
from pathlib import Path

# -> an image API http://shibe.online/api/shibes

"""
    -> he uses the Shibes URL for this, and extracts the URL of one dog image
    -> his result is a list which contains the url of one dog image
    -> we can get around the list by removing the []'s around it - this will convert it into a string
    -> Python3 -m venv venv 
        -> -m STANDS FOR MODULE 
    -> the browser is a tool for making GET requests 
        -> making a request to the location, with specific parameters
            -> e.g I only want the URL of one dog image returned
            -> this returns JSON objects (JavaScript Object Notation)
            -> most urls are GET requests
            -> we can make them with the browser, or with the Python requests package 
            -> you can do this in Python, or with the browser
                -> if you go to the API url in the browser 
                -> 201 means the API request has returned something 
                -> we can also do this in Python, by using an http GET request 
                    -> the result of this is an object 
                    -> a part of the object returned is the url 
                        -> it also includes the type of response which we have received 
                        -> you can ask it for the status_code attribute of the object returned
                            -> this is 200 (meaning that the request succeeded)
                        -> he then uses a method on it, to convert it into a json 
                            -> he operates on it until it looks the same as in the browser, in Python 
    -> running the script again makes a new get request
        -> using debugging (pdb, Python debugger)
            -> the breakpoint() function 
            -> we put this in the code 
            -> he isn't using the debugger built into the IDE
                -> VSCode in his case
                -> we are using Pycharm and a different API, that actually works for URLs of dog images
        -> he is using the debugger, because every time the code is run, there is a different dog image URL being
            generated
            -> different keywords are required for this 
                -> n, c and p for next, contibue and print
                -> TRY AND USE THE breakpoint() FUNCTION, RATHER THAN PRINTING IN THE CODE
                    -> THIS WILL ENTER pdb, THE PYTHON DEBUGGER 
            -> you can enter Python into the terminal, by typing Python
                -> >>> then appears, and you can use it like a calculator 
                -> one caveat with this calculator is that it only works on a computer 
                    -> with lists, you can include numbers and strings 
                -> he then converts it from a list into a string (the url of the dog image) 
            -> PyCharm can do the virtual environments automatically
                -> apparently it is more advanced for this than VSCode
                -> there are many ways of doing things, and he suggests the methods that are the cleanest 
                -> DON'T USE PRINT IN THE CODE TO FIND THE VALUES OF VARIABLES, USE THE breakpoint() FUNCTION 
            -> he then goes through everything we have done 
                -> summarising it 
                    -> first generating the dog image URL from the API online, and then in Python, through making a 
                        GET request to it  
"""

img_url = dict(requests.get("https://dog.ceo/api/breeds/image/random").json())["message"] #a string
# print(img_url)
# breakpoint() #this is better than using print(img_url), because we can also do other things with it

# -> a quotes API http://quotes.stormconsultancy.co.uk/random.json

"""
    -> for some reason, the APIs he suggests don't work 
    -> I am going online and finding my own API for this 
        -> the first which comes up for this is https://api-ninjas.com/api/quotes
        -> there are free and paid versions of the API
            -> they have to be written, and then hosted on external servers
            -> when you look for APIs like this, you want ones which don't require a key 
    -> https://zenquotes.io/api/random
    -> try using the breakpoint() function to debug this, and not print()
    -> YOU NEED TO USE A VPN FOR THIS, OR IT WILL TELL YOU THAT YOU ARE MAKING TOO MANY REQUESTS TO THE API
        -> THIS IS WHY THE BREAKPOINT FUNCTION IS IMPORTANT, OR IT WILL MAKE A NEW REQUEST EVERY TIME THE CODE IS 
            RUN / TESTED IF THIS IS DONE WITH THE PRINT FUNCTION, MORE GET REQUESTS WILL BE MADE 
    -> we have used a different API to him for this
        -> HE CONTINUALLY STRESSES THE IMPORTANCE OF LOOKING AT THE API DOCUMENTATION
        -> the APIs he uses in the tutorial are from 4 years ago / don't work / are outdated (using our own ones)
        -> APIS REQUIRE AN INTERNET CONNECTION 
        -> the best thing is to have our own APIs, that way they can't just be discontinued - with other programs we 
            and other people write relying on them 
        -> integrating the second API
            -> he is inspecting the object which it returns 
                -> this is a dictionary
                -> how JSON is represented JavaScript Object Notation
                -> we can just extract the author from the dictionary 
                -> HE IS USING THE PYTHON DEBUGGER, PDB WITH THIS AGAIN 
                    -> THIS IS DONE USING THE breakpoint() FUNCTION  
"""

quote_url_extraction = json.loads(requests.get("https://zenquotes.io/api/random").content.decode('utf-8'))
quote = f"\"{quote_url_extraction[0]["q"]}\" - {quote_url_extraction[0]["a"]}"
    #this uses f string mini language
# print(quote) #random quote
# breakpoint()


# -> inspect those API
# -> get image and quote


# -> create HTML structure

"""
    -> the HTML browser will autocomplete the HTML that we don't do right 
    -> we are creating an HTML structure in Python
        -> there are multiple ways of doing this, one is f strings
    -> this creates an html structure for the webpage 
    -> when the contents of this is pasted into an index.html file, it is a webpage with a paragraph of quote and a 
        dog image
        -> the dog image and the quote have been extracted from APIs
        -> this contents is then written into an HTML file 
"""

html = f"<p>{quote}</p><img src='{img_url}'>" #this contains the contents of an html file
# print(html)

# -> create a new file

"""
    -> we are putting this under the desktop (home) 
    -> to write the html to a new file 
    -> we are also naming the HTML file 
    -> we are creating the file directly on the desktop 
    -> autocomplete (tab) helps with this in the IDE
"""

f = Path().home().joinpath("Desktop").joinpath("index.html") #f (the file path)
f.write_text(html)
# -> write to the file

"""
    -> he is going through what happens when we run the code 
        -> it imports modules
        -> makes two requests, to two different APIS
            -> image and quotes
        -> extracts the information we want from the APIs   
            -> image URL and quote
        -> then creating a new file / path object
        -> this creates an index.html file in the desktop
        -> running this in Safari shows the quote and dog images we pulled from the APIs
            -> the image is in the same size we pulled from the internet
            -> running the Python again makes different requests and populates the webpage with new information 
            -> we can make the string uppercase in the html file
        -> we can also restrict the image size 
            -> running and reloading this will change the webpage appearance 
            -> this can be done without CSS
        -> this is intermetiate Python  
            -> auto-generating a webpage
            -> OOP <- next 
                -> what objects are 
                -> creating our own objects  
"""


