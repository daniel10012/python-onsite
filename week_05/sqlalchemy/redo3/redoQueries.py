import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from config import username, password
from redoCreate import users_cars, users, cars
from pprint import pprint


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/car_dealership2'

engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()
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

"use a join to select the first name and car model of every user who has bought a car"

#https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_joins.htm

j = users_cars.join(users, users_cars.columns.userID == users.columns.id).join(cars, cars.columns.id == users_cars.columns.carID)
query = db.select([users.columns.first_name, cars.columns.model]).select_from(j)
result = connection.execute(query).fetchall()
print(result)

"use a join to select the first and last name of everyone who has bought a red car"

query2 = db.select([users.columns.first_name, users.columns.last_name]).select_from(j).where(cars.columns.color == 'red')
result2 = connection.execute(query2).fetchall()

print(result2)

"use an insert statement to create a new record in each table"

# query3 = db.insert(cars).values(make="Lamborghini", model='Gallardo', color="red", year="2005")
# connection.execute(query3)

# query4 = db.insert(users).values(first_name = "Ziggy", last_name = "Zoulou")
# connection.execute(query4)

# query5 = db.insert(users_cars)
# new_records = [{'userID': 6 , 'carID': 5},
#                {'userID': 6 , 'carID': 6}]
# connection.execute(query5,new_records)

"use sql to update a record in the 'cars' table"

# query6 = db.update(cars).values(make = "Lombirgoni").where(cars.columns.make == "Lamborghini")
# connection.execute(query6)

"- delete one record from the database"

query7 = db.delete(users).where(users.columns.first_name == "Bob")
connection.execute(query7)