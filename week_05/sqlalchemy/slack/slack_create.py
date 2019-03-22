'''

Building on the example more_APIs/00_slack, make a new database with two tables to model this object:

{
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
}

Think about what tables are required to model this object. Do you need two tables? Three?

Now, instead of saving the list of these objects to a JSON file, persist the data
to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''


from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table,Column, Integer, String, Boolean, SmallInteger, Date
from config import username, password

from pprint import pprint


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/slack'

engine = create_engine(DATABASE_URI,echo=True)
connection = engine.connect()
metadata = MetaData()

threads = Table('threads', metadata,
                 Column('msg_id',String()),
                 Column('id', Integer(),autoincrement=True, primary_key=True),
                 Column('link', String(), nullable=False),
                 Column('description', String()),
                 Column('date_added',Date()),
                 Column('read', Boolean, default=False),
                 Column('rating', Integer(), default=0),
                 Column('starred', Boolean, default=False)
                 )

comments = Table('comments', metadata,
                 Column('id', Integer(),autoincrement=True, primary_key=True),
                 Column('comment', String()),
                 Column('thread_id',Integer()),
                 )

metadata.create_all(engine)

