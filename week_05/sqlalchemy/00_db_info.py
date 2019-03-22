'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
from config import *
from pprint import pprint

engine = sqlalchemy.create_engine(f'postgresql://{username}:{password}@localhost/dvdrentals')
connection = engine.connect()
metadata = sqlalchemy.MetaData()


film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

#print(film.columns.keys())
#print(repr(metadata.tables['film']))

query = sqlalchemy.select([film]).order_by(sqlalchemy.asc(film.columns.film_id))
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

###################################################

category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([category]).order_by(sqlalchemy.asc(category.columns.category_id))
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)