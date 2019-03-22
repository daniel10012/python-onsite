'''
Redo the exercises from '03_pgadmin.txt' in the SQL labs using SQLAlchemy .

'''

'''Using pgadmin:

- create a new blank database with the name "car_dealership2" '''


from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table,Column, Integer, String, Boolean, SmallInteger, Date
from config import username, password
from pprint import pprint


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/car_dealership2'

engine = create_engine(DATABASE_URI,echo=True)
connection = engine.connect()
metadata = MetaData()

users_cars = Table('users_cars', metadata,
                 Column('id', Integer(),autoincrement=True, primary_key=True),
                 Column('userID', Integer(), nullable=False),
                 Column('carID', Integer()),
                 )

users = Table('users', metadata,
                 Column('id', Integer(),autoincrement=True, primary_key=True),
                 Column('first_name', String(), nullable=False),
                 Column('last_name', String()),
                 )

cars = Table('cars', metadata,
                 Column('id', Integer(),autoincrement=True, primary_key=True),
                 Column('make', String(), nullable=False),
                 Column('model', String()),
                 Column('color', String()),
                 Column('year', Integer())
                 )

metadata.create_all(engine)

'''

- create a new table named "users_cars" with the following fields:
    - id (auto increment)
    - userID (refers to "id" in users table)
    - carID (refers to "id" in cars table)


- create a new table named "users" with the following fields
    - id (auto increment)
    - first name
    - last name

- create a new table named "cars" with the following fields
    - id (auto increment)
    - make
    - model
    - color
    - year

- populate these tables with at least 5 records each - the more the merrier

- Write the SQL queries to accomplish the following: (write each of your queries below for review)

    - select all records from users

    SELECT * FROM users;


    - select all records from cars where car make = "Toyota"

    SELECT * FROM cars WHERE make = 'toyota';


    - use a join to select the first name and car model of every user who has bought a car

    SELECT users."first name", cars.model
FROM cars
	INNER JOIN users_cars
	ON cars.id = users_cars."carID"
		INNER JOIN users
		ON users_cars."userID"=users.id


    - use a join to select the first and last name of everyone who has bought a red car

    SELECT users."first name", users."last name"
FROM cars as c
	INNER JOIN users_cars as uc
	ON c.id = uc."carID"
		INNER JOIN users as u
		ON uc."userID"=u.id
		WHERE c.color = 'red';

    - use an insert statement to create a new record in each table

INSERT INTO cars (make,model,color,year)
VALUES ('lada','turbo','red',1990);

INSERT INTO users ("first name", "last name")
VALUES ('jean','mich');

INSERT INTO users_cars ("userID","carID")
VALUES (6,6);

    - use sql to update a record in the "cars" table

    UPDATE cars
SET model = 'turbomax', year = 1996
WHERE id = 6;

    - delete one record from the database

DELETE FROM cars WHERE make = 'lada';'''