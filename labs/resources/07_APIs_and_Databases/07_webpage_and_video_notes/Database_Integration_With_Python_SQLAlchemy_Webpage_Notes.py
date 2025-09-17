"""
    -> outline
        -> install SQLALchemy
        -> import the Sakila database
        -> connect to the database
            -> PostgreSQL connection
            -> MySWL connection
        -> accessing database metainformation
        -> reading with the SELECT statement / query
        -> using WHERE, IN, AND and AND NOT to filter results
        -> using JOINS
        -> creating a database table
        -> using the INSERT statement to insert multiple records
        -> the UPDATE statement; DELETE statement to delete tables
        -> accessing result proxy fields, and then mapping them to objects
        -> database integration with SQLALchemy

    -> THE SQL AND DATABASES COURSE IS A PRE-REQUISITE FOR THIS ONE
    -> integrating Python applications with databases using SQLAlchemy
    -> we are using the free Sakila database with MySQL for this
    -> SQLAlchemy is for integrating databases into Python, and Sakila is a database which is free to use as a part of this
    -> THIS IS FOR RELATIONAL DATABASES
    -> it is a PYTHON DATABASE CONNECTOR
        -> this can be used with SQL databses
        -> MySQL, PostgreSQL, Oracle
    -> this section is connecting to a MySQL database
    -> pip install sqlalchemy <- to install sqlalchemy
    -> the sakila database contains information about films, actors, rentals and payments
    -> we need to install a driver so that SQLAlchemy can connect to the database
        -> pip install pymysql
        -> we are also downloading the database from the internet
    -> we first connect to the database
        -> sqlalchemy IS A PYTHON MODULE
        -> THIS IS USED FOR IMPORTING AND INTERACTING WITH DATABASES
        -> connecting to the database
    -> YOU NEED TO HAVE A VIRTUAL ENVIRONMENT ALREADY ACTIVATED
    -> we need a virtual environment activated
        -> and then to pip install sqlalchemy and pymysql into this
"""

import sqlalchemy #import the sqlalchemy package

#establish a metadata object and a connection object
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()

#matadata objects are used to create able objects
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine) #this creates an actor object
    #we load with the engine stored in the `engine` variable
print(actor.columns.keys()) #this prints information about the `actor` table in the sakila database
    #this returns the collumn names of the actor table
    #['actor_id', 'first_name', 'last_name', 'last_update']





