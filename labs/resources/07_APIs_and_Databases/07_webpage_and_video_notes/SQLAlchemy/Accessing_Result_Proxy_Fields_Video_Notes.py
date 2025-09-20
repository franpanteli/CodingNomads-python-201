"""Accessing Result Proxy Fields Video Notes
    -> accessing proxy fields
        -> using the .fetchall() method, vs the fetchone() method
        -> we get back the first row from the result proxy when the fetchone() method is used
        -> we can iterate through the fetchone() result to get the same results as the fetchall() method
            -> this iterates through each object
            -> EACH OF THESE RESULTS IS A RESULT PROXY OBJECT
                -> these can be accessed through their IDs in the database
                -> the results of this are then printed
            -> we can also access the keys from this
            -> results can also be accessed by printing out the data by the name of the collumn in the set
        -> he runs the code and this provides a summary
            -> we are seeing if we can do this for each of the results in the loop
            -> for result in result_proxy
                -> he is printing out the first and last names of the actors in the database, by using the column name
"""

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([actor])
result_proxy = connection.execute(query)

result = result_proxy.fetchone()
pprint(result['first_name']) #accessing the elements by their first name

for result in result_proxy:
    print(f"First name: {result['first_name']})
    print(f"First name: {result['last_name']})
    print() #now we are accessing the first and last names of the actors by accessing the column or key name

# result_set = result_proxy.fetchone() #this is the result proxy
# print(result_set)

# for result in result_proxy:
#     print(type(result)) #these are result proxy objects

#THE KEYS ARE THE COLUMN NAMES IN THE DATABASE