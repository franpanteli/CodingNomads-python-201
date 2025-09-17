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
from pprint import pprint

#establish a metadata object and a connection object
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()

#matadata objects are used to create able objects
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine) #this creates a table object
    #we load with the engine stored in the `engine` variable
# print(actor.columns.keys()) #this prints information about the `actor` table in the sakila database
    #this returns the collumn names of the actor table
    #['actor_id', 'first_name', 'last_name', 'last_update']

"""
    -> the SELECT query
        -> we are reading data 
        -> querying the data (asking the database questions)
        -> we create a SELECT statement 
        -> then execute the query with the execute() method 
        -> the result is saved in the result_proxy variable 
        -> results are fetched, by using the fetchall() method 
"""

query = sqlalchemy.select(actor) #this is equivalent to the sql: SELECT * FROM the actor table object we just created
result_proxy = connection.execute(query) #execute the query defined in the previous line
    #this is the connection obejct
    #you can't just print this out, you have to use the fetchall() or fetchmany() method, and then print the results of this

result_set = result_proxy.fetchall() #fetch the results of the database query stored in the `result_proxy` variable
# pprint(result_set) #print out the result #this uses the pretty print module, to print out the information on multiple lines, rather than one
    #this can then be used as any other Python object
    #we can use this to iterate through each of the elements in the database, for example
    #fetchmany() is used for large datasets, instead of fetchall()
        # result_set = result_proxy.fetchmany(5) #this contains the number of rows which we want to fetch from the database

#OUTPUT
# ['actor_id', 'first_name', 'last_name', 'last_update']
# [(1, 'PENELOPE', 'GUINESS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (2, 'NICK', 'WAHLBERG', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (3, 'ED', 'CHASE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (4, 'JENNIFER', 'DAVIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (5, 'JOHNNY', 'LOLLOBRIGIDA', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (6, 'BETTE', 'NICHOLSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (7, 'GRACE', 'MOSTEL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (8, 'MATTHEW', 'JOHANSSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (9, 'JOE', 'SWANK', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (10, 'CHRISTIAN', 'GABLE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (11, 'ZERO', 'CAGE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (12, 'KARL', 'BERRY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (13, 'UMA', 'WOOD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (14, 'VIVIEN', 'BERGEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (15, 'CUBA', 'OLIVIER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (16, 'FRED', 'COSTNER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (17, 'HELEN', 'VOIGHT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (18, 'DAN', 'TORN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (19, 'BOB', 'FAWCETT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (20, 'LUCILLE', 'TRACY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (21, 'KIRSTEN', 'PALTROW', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (22, 'ELVIS', 'MARX', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (23, 'SANDRA', 'KILMER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (24, 'CAMERON', 'STREEP', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (25, 'KEVIN', 'BLOOM', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (26, 'RIP', 'CRAWFORD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (27, 'JULIA', 'MCQUEEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (28, 'WOODY', 'HOFFMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (29, 'ALEC', 'WAYNE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (30, 'SANDRA', 'PECK', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (31, 'SISSY', 'SOBIESKI', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (32, 'TIM', 'HACKMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (33, 'MILLA', 'PECK', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (34, 'AUDREY', 'OLIVIER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (35, 'JUDY', 'DEAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (36, 'BURT', 'DUKAKIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (37, 'VAL', 'BOLGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (38, 'TOM', 'MCKELLEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (39, 'GOLDIE', 'BRODY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (40, 'JOHNNY', 'CAGE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (41, 'JODIE', 'DEGENERES', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (42, 'TOM', 'MIRANDA', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (43, 'KIRK', 'JOVOVICH', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (44, 'NICK', 'STALLONE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (45, 'REESE', 'KILMER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (46, 'PARKER', 'GOLDBERG', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (47, 'JULIA', 'BARRYMORE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (48, 'FRANCES', 'DAY-LEWIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (49, 'ANNE', 'CRONYN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (50, 'NATALIE', 'HOPKINS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (51, 'GARY', 'PHOENIX', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (52, 'CARMEN', 'HUNT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (53, 'MENA', 'TEMPLE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (54, 'PENELOPE', 'PINKETT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (55, 'FAY', 'KILMER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (56, 'DAN', 'HARRIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (57, 'JUDE', 'CRUISE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (58, 'CHRISTIAN', 'AKROYD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (59, 'DUSTIN', 'TAUTOU', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (60, 'HENRY', 'BERRY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (61, 'CHRISTIAN', 'NEESON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (62, 'JAYNE', 'NEESON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (63, 'CAMERON', 'WRAY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (64, 'RAY', 'JOHANSSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (65, 'ANGELA', 'HUDSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (66, 'MARY', 'TANDY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (67, 'JESSICA', 'BAILEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (68, 'RIP', 'WINSLET', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (69, 'KENNETH', 'PALTROW', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (70, 'MICHELLE', 'MCCONAUGHEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (71, 'ADAM', 'GRANT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (72, 'SEAN', 'WILLIAMS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (73, 'GARY', 'PENN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (74, 'MILLA', 'KEITEL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (75, 'BURT', 'POSEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (76, 'ANGELINA', 'ASTAIRE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (77, 'CARY', 'MCCONAUGHEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (78, 'GROUCHO', 'SINATRA', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (79, 'MAE', 'HOFFMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (80, 'RALPH', 'CRUZ', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (81, 'SCARLETT', 'DAMON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (82, 'WOODY', 'JOLIE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (83, 'BEN', 'WILLIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (84, 'JAMES', 'PITT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (85, 'MINNIE', 'ZELLWEGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (86, 'GREG', 'CHAPLIN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (87, 'SPENCER', 'PECK', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (88, 'KENNETH', 'PESCI', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (89, 'CHARLIZE', 'DENCH', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (90, 'SEAN', 'GUINESS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (91, 'CHRISTOPHER', 'BERRY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (92, 'KIRSTEN', 'AKROYD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (93, 'ELLEN', 'PRESLEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (94, 'KENNETH', 'TORN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (95, 'DARYL', 'WAHLBERG', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (96, 'GENE', 'WILLIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (97, 'MEG', 'HAWKE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (98, 'CHRIS', 'BRIDGES', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (99, 'JIM', 'MOSTEL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (100, 'SPENCER', 'DEPP', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (101, 'SUSAN', 'DAVIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (102, 'WALTER', 'TORN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (103, 'MATTHEW', 'LEIGH', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (104, 'PENELOPE', 'CRONYN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (105, 'SIDNEY', 'CROWE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (106, 'GROUCHO', 'DUNST', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (107, 'GINA', 'DEGENERES', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (108, 'WARREN', 'NOLTE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (109, 'SYLVESTER', 'DERN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (110, 'SUSAN', 'DAVIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (111, 'CAMERON', 'ZELLWEGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (112, 'RUSSELL', 'BACALL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (113, 'MORGAN', 'HOPKINS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (114, 'MORGAN', 'MCDORMAND', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (115, 'HARRISON', 'BALE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (116, 'DAN', 'STREEP', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (117, 'RENEE', 'TRACY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (118, 'CUBA', 'ALLEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (119, 'WARREN', 'JACKMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (120, 'PENELOPE', 'MONROE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (121, 'LIZA', 'BERGMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (122, 'SALMA', 'NOLTE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (123, 'JULIANNE', 'DENCH', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (124, 'SCARLETT', 'BENING', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (125, 'ALBERT', 'NOLTE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (126, 'FRANCES', 'TOMEI', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (127, 'KEVIN', 'GARLAND', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (128, 'CATE', 'MCQUEEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (129, 'DARYL', 'CRAWFORD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (130, 'GRETA', 'KEITEL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (131, 'JANE', 'JACKMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (132, 'ADAM', 'HOPPER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (133, 'RICHARD', 'PENN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (134, 'GENE', 'HOPKINS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (135, 'RITA', 'REYNOLDS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (136, 'ED', 'MANSFIELD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (137, 'MORGAN', 'WILLIAMS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (138, 'LUCILLE', 'DEE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (139, 'EWAN', 'GOODING', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (140, 'WHOOPI', 'HURT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (141, 'CATE', 'HARRIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (142, 'JADA', 'RYDER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (143, 'RIVER', 'DEAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (144, 'ANGELA', 'WITHERSPOON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (145, 'KIM', 'ALLEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (146, 'ALBERT', 'JOHANSSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (147, 'FAY', 'WINSLET', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (148, 'EMILY', 'DEE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (149, 'RUSSELL', 'TEMPLE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (150, 'JAYNE', 'NOLTE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (151, 'GEOFFREY', 'HESTON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (152, 'BEN', 'HARRIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (153, 'MINNIE', 'KILMER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (154, 'MERYL', 'GIBSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (155, 'IAN', 'TANDY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (156, 'FAY', 'WOOD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (157, 'GRETA', 'MALDEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (158, 'VIVIEN', 'BASINGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (159, 'LAURA', 'BRODY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (160, 'CHRIS', 'DEPP', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (161, 'HARVEY', 'HOPE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (162, 'OPRAH', 'KILMER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (163, 'CHRISTOPHER', 'WEST', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (164, 'HUMPHREY', 'WILLIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (165, 'AL', 'GARLAND', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (166, 'NICK', 'DEGENERES', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (167, 'LAURENCE', 'BULLOCK', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (168, 'WILL', 'WILSON', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (169, 'KENNETH', 'HOFFMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (170, 'MENA', 'HOPPER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (171, 'OLYMPIA', 'PFEIFFER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (172, 'GROUCHO', 'WILLIAMS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (173, 'ALAN', 'DREYFUSS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (174, 'MICHAEL', 'BENING', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (175, 'WILLIAM', 'HACKMAN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (176, 'JON', 'CHASE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (177, 'GENE', 'MCKELLEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (178, 'LISA', 'MONROE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (179, 'ED', 'GUINESS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (180, 'JEFF', 'SILVERSTONE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (181, 'MATTHEW', 'CARREY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (182, 'DEBBIE', 'AKROYD', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (183, 'RUSSELL', 'CLOSE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (184, 'HUMPHREY', 'GARLAND', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (185, 'MICHAEL', 'BOLGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (186, 'JULIA', 'ZELLWEGER', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (187, 'RENEE', 'BALL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (188, 'ROCK', 'DUKAKIS', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (189, 'CUBA', 'BIRCH', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (190, 'AUDREY', 'BAILEY', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (191, 'GREGORY', 'GOODING', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (192, 'JOHN', 'SUVARI', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (193, 'BURT', 'TEMPLE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (194, 'MERYL', 'ALLEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (195, 'JAYNE', 'SILVERSTONE', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (196, 'BELA', 'WALKEN', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (197, 'REESE', 'WEST', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (198, 'MARY', 'KEITEL', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (199, 'JULIA', 'FAWCETT', datetime.datetime(2006, 2, 15, 4, 34, 33)),
#  (200, 'THORA', 'TEMPLE', datetime.datetime(2006, 2, 15, 4, 34, 33))]

"""
    -> filtering results 
        -> filtering the results from the SELECT statement 
        -> SQLALCHEMY IS FOR INTERACTING WITH DATABASES IN PYTHON 
        -> WHERE 
            -> in SQL: SELECT * FROM sakila.actor WHERE first_name = "PENELOPE";
                -> select all from the actors table where the first name is PENELOPE
            -> in sqlalchemy: sqlalchemy.select(actor).where(actor.columns.first_name == 'PENELOPE') 
                -> select the actors table where the first name is PENELOPE
        -> IN 
            -> SQL: SELECT * FROM sakila.actor WHERE first_name IN ("PENELOPE", "JOHN", "UMA");
                -> select all from the actors table, where the first name is in this list of names 
            -> sqlalchemy: sqlalchemy.select(actor).where(actor.columns.first_name.in_(["PENELOPE", "JOHN", "UMA"]))
                -> select from the actors table where the first name is in this list (the same meaning as in SQL)
        -> AND, and AND NOT
            -> in SQL
                -> SELECT * FROM sakila.film WHERE length > 60 AND rating = "PG";
                    -> select all of the elements from this database where the length is > 60 and the rating is "PG"
                -> SELECT * FROM sakila.film WHERE length > 60 AND NOT rating = "PG";
                    -> this is the same as the previous statement, but it uses AND NOT and not AND 
            -> in Python sqlalchemy 
                -> sqlalchemy.select(film).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating == "PG"))
                    -> select a film where the database and the length of the element in that column is more than 60, and the rating is PG
                -> sqlalchemy.select(film).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating != "PG"))
                    -> unlike in SQL, THESE SELECT STATEMENTS IN PYTHON ARE SET EQUAL TO VARIABLES 
                    -> this is the same as in the previous statement, but with != instead of ==
                    -> it is a boolean statement 
                -> SQLALCHEMY IS A PYTHON MODULE FOR IMPORTING DATABASES IN SQL
        -> ORDER BY 
            -> SQL: SELECT * FROM sakila.film ORDER BY replacement_cost ASC;
                -> select all of the columns from this database and order them by the values in the `replacement_cost` column
            -> sqlalchemy: sqlalchemy.select(film).order_by(sqlalchemy.asc(film.columns.replacement_cost))
                -> use the sqlalchemy Python module, select the elements in this column and order them by the value of the items in the replacement_cost column
        -> SUM()
            -> SQL: SELECT SUM(length) FROM sakila.film;
                -> THE SUM FUNCTION RETURNS THE SUM OF A GIVEN FIELD 
                -> select the sum of the length of elements from the film column in the Salkila database 
            -> sqlalchemy: sqlalchemy.select(sqlalchemy.func.sum(film.columns.length))
                -> this can be set equal to a variable in Python 
                -> use the sqlalchemy module to perform the sum function on the films collunm 
                -> this function calculates the length of entries in this column of the database 
"""

