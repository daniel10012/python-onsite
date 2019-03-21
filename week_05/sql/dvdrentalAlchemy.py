import sqlalchemy as sqa
from secrets import username, password
from pprint import pprint


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/dvdrentals'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()


#Select all the actors with the first name of your choice

