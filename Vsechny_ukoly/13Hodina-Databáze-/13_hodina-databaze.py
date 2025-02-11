import sqlite3


def db_insert(db_cur, table, cols, vals):
    # check table
    if len(cols) != len(vals):
        return False

    columns = ""
    for item in cols:
        columns += f"{item},"

    values = ""
    for item in vals:
        values += f"'{item}',"

    query = f"""INSERT INTO {table} ({columns[:-1]}) VALUES ({values[:-1]})"""
    db_cur.execute(query)

    return True


conn = sqlite3.connect("my_db.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20),
            age INTEGER);
""")

cur.execute("""INSERT INTO users (name, age) VALUES (?, ?);""", ("Jan", 33))
db_insert(cur, "users", ("name", "age"), ("Adam", 22))

conn.commit()

cur.execute("""SELECT * FROM users;""")
data = cur.fetchall()

print(data)

conn.close()