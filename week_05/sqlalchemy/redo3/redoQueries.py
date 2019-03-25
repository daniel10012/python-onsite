import sqlalchemy as sqa
from sqlalchemy.orm import sessionmaker
from config import username, password
from redoCreate import users_cars, users, cars
from pprint import pprint

DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/car_dealership2'

engine = sqa.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = sqa.MetaData()
Session = sessionmaker(bind=engine)
session = Session()

# SELECT * FROM users;


# query = sqa.select([users])
# result_proxy = connection.execute(query)
#
# result_set = result_proxy.fetchall()
# pprint(result_set)

# SELECT * FROM cars WHERE make = 'toyota';

# query = sqa.select([cars]).where(cars.columns.make == 'Toyota')
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)

# use a join to select the first name and car model of every user who has bought a car


#query2 = sqa.select([users.columns.first_name, cars.columns.model], users.columns.id == users_cars.columns.userID , cars.columns.id == users_cars.columns.carID))

# q = sqa.select([users, cars],users.columns.id == users_cars.columns.userID)
# r = sqa.select([users.columns.first_name, cars.columns.model], cars.columns.id == q.columns.carID)
# result_proxy = connection.execute(r)
#
# result_set = result_proxy.fetchall()
# print(result_set)

q = session.query(users).filter(users.columns.id == users_cars.columns.userID)
filter(cars.columns.id == users_cars.columns.carID)
filter(cars.model == 'Toyota')