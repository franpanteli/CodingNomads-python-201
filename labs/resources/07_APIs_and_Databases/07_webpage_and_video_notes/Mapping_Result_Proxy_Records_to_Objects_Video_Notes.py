"""Mapping result proxy records to objects video notes
    -> mapping data to Python objects
    -> see actor.py for the class written to model this data
    -> A CLASS IS DEFINED WHICH MODELS ACTORS IN THE DATABASE WITH ACTOR OBJECTS
        -> THIS IS DEFINED IN ANOTHER .PY FILE, actor.py, WHICH IS IMPORTED IN ON THE SECOND LINE OF THE CODE
            -> WE IMPORT THE actor.py FILE AND THE Actor CLASS FROM THIS
    -> this is so that the information about the actors is can be stored inside an actor object (in this case, for this database - Sakila)
        -> this allows us to define methods in the class definition, which can be used to operate on the Actor objects 
"""

import sqlalchemy
from actor import Actor #import the Actor class we defined in actor.py
from pprint import pprint

#this is standard code for working in SQLALchemy
    #these three lines go at the first of every exercise in this webpage
    #SQLAlchemy is SQL, in Python
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila') #create the engine
connection = engine.connect() #connect to the database
metadata = sqlalchemy.MetaData() #create metadata object

#create the actor table
actor = sqlalchemy.Table('actor', metadata,autoload=True, autoload_with=engine)
    #the arguments to this are the variables we just created <- the name of the table, the database metadata object and the engine we want to use to load it with

query = sqlalchemy.select([actor]) #select the actors table
result_proxy = connection.execute(query) #ececute the query

actor_list = []

for result in result_proxy: #iterate through results and print out the first and last names of the actors
    #we defined an actor class which we are importing in that has done this in a string dunder method
    # print(f"First name: {result['first_name']})")
    # print(f"Last name: {result['last_name']})")
    # print()

    new_actor = Actor(result['actor_id'], result['first_name'], result['last_name'], result['last_update'])
        #we create a new actor object, using the Actor class defined in the actor.py file
        #this is done to model the Salkila database
        #a for loop is used to iterate through the database elements for this
        #A CLASS CAN BE USED TO MODEL THE DATA IN A DATABASE
            #IT IS DEFINED IN A NEW .py FILE AND IMPORTED IN
            #it doesn't have to be defined in a new .py file, this is for the sake of reusable code

    actor_list.append(new_actor) #populate the actor_list with the actor object we are currently iterating through

# print(actor_list) #printing out the list with the actor objects

#the result of this is not readable
    #we iterate through the actor list and print out the results to fix this
    #this puts one actor object on each line

for actor in actor_list:
    print(actor)
















