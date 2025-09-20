"""DELETE Statement
    -> the delete statement
    -> deleting one or more records from a table
        -> this is done using the `delete` and `where` keywords
        -> this is used to delete all records from the table newTable, where the salary column < 100,000
    -> he changes the code he wrote in the previous section
    -> deleting, rather than updating, methods
    -> deleting everything where the salary is < 100,000, and then executing this query
    -> he looks into the database and this shows the element was deleted
"""

# import modules
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila') #create an engine to connect to the Sakila database
connection = engine.connect() #connect to the Sakila database
metadata = sqlalchemy.MetaData() #record object metadata

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine) #create a new table, called newTable

query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 100000) #use the delete method to delete columns in the table we just created, on the condition that the salary is less than 100,000
results = connection.execute(query) #execute the query we just defined


