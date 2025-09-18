"""DELETE Statement
    -> 
"""

# import modules
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 100000)
results = connection.execute(query)
