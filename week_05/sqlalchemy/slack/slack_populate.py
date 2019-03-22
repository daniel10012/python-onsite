from slack_fetching import get_list_messages
import sqlalchemy as sqa
from config import username, password


DATABASE_URI = f'postgres+psycopg2://{username}:{password}@localhost:5432/slack'

engine = sqa.create_engine(DATABASE_URI,echo=False)
connection = engine.connect()
metadata = sqa.MetaData()

threads = sqa.Table('threads',metadata,autoload=True,autoload_with=engine)

#query = sqa.insert(threads)
info = get_list_messages()

for dict in info:
    del dict["comments"]
    query = sqa.select([threads]).where(threads.columns.msg_id == dict["msg_id"])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    if result_set == []:
        query2 = sqa.insert(threads)
        connection.execute(query2,[dict])