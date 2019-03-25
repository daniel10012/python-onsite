import sqlalchemy as sqa
from config import username, password
from redoCreate import users_cars, users, cars



DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/car_dealership2'

engine = sqa.create_engine(DATABASE_URI,echo=True)
connection = engine.connect()
metadata = sqa.MetaData()


users_cars_info = [{'userID': 1 , 'carID': 2},
                    {'userID': 1 , 'carID': 4},
                    {'userID': 2 , 'carID': 3},
                    {'userID': 3 , 'carID': 2},
                    {'userID': 3 , 'carID': 4},
                    {'userID': 4 , 'carID': 5},
                    {'userID': 5 , 'carID': 1},
                    {'userID': 5 , 'carID': 3}
                    ]

query1 = sqa.insert(users_cars)
connection.execute(query1, users_cars_info)


users_info = [{'first_name': 'Bob' , 'last_name': 'Zing'},
                {'first_name': 'James' , 'last_name': 'Fung'},
                {'first_name': 'George' , 'last_name': 'Minf'},
                {'first_name': 'Roger' , 'last_name': 'Zulu'},
                {'first_name': 'Mike' , 'last_name': 'Popo'}
                    ]

query2 = sqa.insert(users)
connection.execute(query2, users_info)



cars_info = [{'make': 'Toyota', 'model': 'Prius', 'color': 'red', 'year': 1990},
                {'make': 'Lada', 'model': 'Maxi', 'color': 'blue', 'year': 1996},
                {'make': 'Peugeot', 'model': '306', 'color': 'pink', 'year': 2016},
                {'make': 'Jaguar', 'model': 'xj220', 'color': 'purple', 'year': 1985},
                {'make': 'GM', 'model': 'Rover', 'color': 'yellow', 'year': 2000}
                    ]

query3 = sqa.insert(cars)
connection.execute(query3, cars_info)