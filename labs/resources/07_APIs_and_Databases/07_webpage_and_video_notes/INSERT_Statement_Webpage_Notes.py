"""
    -> the INSERT statement
        -> inserting data into the table
        -> a table is first created, and then populated with data
        -> to see if this is successful, we go into the Sakila database and see if the new table is there
"""

#import modules
import sqlalchemy

#establish a connection to the table
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect() #connect to the database
metadata = sqlalchemy.MetaData() #create the metadata object

newTable = sqlalchemy.Table('newTable', metadata, autoload_with=engine) #define the new table
    #we are going to populate this with data later

query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=60000.00, active=True) #use the insert() method and pass in the key-value pairs
    #the keys are the column names and the values are the new values which are going to be inserted
    #we are inserting into the new table and telling it what values we want entered
result_proxy = connection.execute(query)
connection.commit()

"""Inserting multiple records
    -> we change the syntax if we want to insert multiple records
    -> we create a list for the new records 
    -> we are passing in two lists as part of this
    -> the query object is then passed these new table records / entries
    -> this is inserting multiple records into the table with one execution 
"""

# query = sqlalchemy.insert(newTable)
# new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
#                {'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
# result_proxy = connection.execute(query,new_records)


