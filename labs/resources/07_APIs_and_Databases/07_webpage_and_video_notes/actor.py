"""Mapping result proxy records to objects video notes CONTINUED
    -> mapping data to Python objects
    -> WE WANT TO CREATE A CLASS TO MODEL THE DATA
    -> we are saying 'the general database entry looks like this, now we will create this method to model an actor with this name etc in the Sakila database'
    -> this is defined in the other
"""

class Actor: #for actor objects

    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    #creating a dunder method for printing the object

    def __str__(self):
        return f"First name: {self.first_name} {self.last_name}, was updated: {self.last_update}"
        #we can have this print out any information about the actor which we like