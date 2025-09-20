"""UPDATE Statement
    -> to update a record in the database
    -> we update the salary column in the newTable table, where the Id column is equal to one
    -> we are defining the query using the update() method
    -> we are updating the value in the new table
    -> telling it the value we want to update
    -> we are updating the salary column in newTable
    -> we aren't updating all the salaries, only one record
    -> we then executes this query, by using the .connection() method
    -> to see the output of this, he goes into the Sakila database and views the changes
"""

#import modules
import sqlalchemy

#create the engine object
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')

#establish a connection to the database
connection = engine.connect()

#establish object to store metadata
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

#the update and where methods are used with this
    #update the table where the values have a certain salary, and the column Id is 1
query = sqlalchemy.update(newTable).values(salary=100000).where(newTable.columns.Id == 1)

#execute the query
result = connection.execute(query)
