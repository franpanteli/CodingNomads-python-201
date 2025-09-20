#import modules
import sqlalchemy

"""
    -> creating a new table, rather than using an existing one 
    -> we establish the connection and the metadata object
    -> then create a new table 
        -> we specify the name of the table
        -> then the columns which the new table is going to have 
        -> we pass in the name of the column and rules which we need to set about the data that they contain 
        -> we want the elements of the table to be integers, in the first column 
        -> we then create a name 
            -> SQLAlchemy 
            -> he uses a string up to size 255 characters
            -> then adds the nullable argument to this
                -> it is not going to be nullable 
            -> he proceeds to add the rest of the columns to this 
        -> he then uses the metadata object to create a function and pass it to the engine
        -> THE ENGINE IS WHAT INTERACTS WITH THE DATABASE
            -> he then goes into the Sakila database to see if the new table was created 
"""
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila') #create the engine
connection = engine.connect() #connect to the database
metadata = sqlalchemy.MetaData() #use the MetaData method to log the metadata when the database connection is made

#creating a new table
    #SQLAlchemy creates a table if it doesn't already exist
newTable = sqlalchemy.Table('newTable', metadata,
                            sqlalchemy.Column('Id', sqlalchemy.Integer()),
                            sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
                            sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0),
                            sqlalchemy.Column('active', sqlalchemy.Boolean(), default=True)
                            )

metadata.create_all(engine)
