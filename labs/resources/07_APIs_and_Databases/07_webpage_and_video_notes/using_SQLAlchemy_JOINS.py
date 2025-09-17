"""
    -> using JOINS
        -> JOIN STATEMENTS ALLOW YOU TO SELECT DATA FROM MORE THAN ONE TABLE
        -> using SQLAlchemy joins TO FIND DATA WHICH TWO TABLES HAVE IN COMMON
        -> we are looking for data which the actor and film tables have in common
"""

# import modules
import sqlalchemy
from pprint import pprint

#define the `engine` variable and establish a connection to the database
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

#create tables
    #create the actor table object
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)

    #create the film table object
film = sqlalchemy.Table('film', metadata, autoload_with=engine)

    #create the film_actor table object
film_actor = sqlalchemy.Table('film_actor', metadata, autoload_with=engine)

#joining the two tables together with SQLAlchemy
    #use the SQLAlchemy table method to find the data which the two tables have in common

join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
    #use SQLAlchemy (the module of SQL in Python) with the join method to join these two tables
    #we join them by the film id information
    #this is the information which the two tables have in common

query = sqlalchemy.select(film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name).select_from(join_statement)
    #using SQLAlchemy to select this information

result_proxy = connection.execute(query) #connect the query to the database

result_set = result_proxy.fetchall() #fetch the information from the query
pprint(result_set) #the output from this is hundreds of lines that look like this:  (811, 'SMILE EARRING', 'JEFF', 'SILVERSTONE')
    #this is done with the pretty print module, so all of the information prints on separate lines, and not one

"""
    -> JOIN queries video notes 
        -> performing a join statement, rather than just selecting from one table 
        -> selecting all the actors and all the films they were in 
        -> selecting a specific actor and the films they were in 
        -> we join the actor table with the film actor table, then the film actor table with the film table 
            -> WE ARE MAKING MULTIPLE JOINS
            -> THERE ARE TWO JOIN STATEMENTS REQUIRED FOR THIS 
        -> TABLE OBJECTS ARE FIRST CREATED FOR THIS 
        -> then creating the join statement 
            -> this is what is used to set up the query 
            -> we will select the film names and then the actor names 
        -> starting by using one table 
            -> actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)))
                -> we are joining the film actor object
                -> WE ARE JOINING THE TWO TABLES ON A CONDITION, THAT THE ACTOR ID MATCHES THE FILM ID 
                -> this joins the film actor table with the actor table 
        -> then joining this with the film table 
            -> this is done by using the join_actor_film_actor varible 
            -> this variable is then joined with another join statement in SQLAlchemy 
            -> we are joining the object we just created with the film object
                -> joining the film object on the condition that the IDs in the two tables match 
                -> WHENEVER JOINS ARE PERFORMED, AND MULTIPLE JOINS CAN BE USED, TWO TABLES ARE ALWAYS JOINED ON SOME STATEMENT 
                -> sqlalchemy.select()
                    -> we are selecting specific collumns from the join statement 
                    -> we are selecting from columns which we write in the code
                    -> there are the columns we want to select, and then there is where we want to select them from 
        -> then creating the result proxy, the result set and printing out the result set
            -> fetching the results and pretty printing them 
            -> we get the first name of the actor, in this case, and all of the films they are in
            -> it does this for all of the actors in the table 
"""
