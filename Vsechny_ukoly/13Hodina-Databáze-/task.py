import sqlite3
from task_data import *
from task_table import *

conn = sqlite3.connect("chat_app.db")

cur = conn.cursor()

cur.execute(users_create_table)
cur.execute(rooms_create_table)
cur.execute(messages_create_table)
cur.execute(insert_users)
cur.execute(insert_rooms)
cur.execute(insert_messages)
conn.commit()

