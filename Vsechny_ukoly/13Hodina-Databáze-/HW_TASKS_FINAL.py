import sqlite3

#Task 1: Nájsť používateľov, ktorí poslali správy do konkrétnej miestnosti (napr. room1).

conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()

query = """
SELECT DISTINCT users.username
FROM messages
JOIN users ON messages.user_id = users.id
JOIN rooms ON messages.room_id = rooms.id
WHERE rooms.name = 'room1';
"""
cur.execute(query)
results = cur.fetchall()

print("Uživatelé, kteří poslali zprávu do room1:")
for row in results:
    print(row[0])

conn.close()


print()

#Task 2: Spočítať, koľko rôznych používateľov poslalo správy do jednotlivých miestností.

conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()

query = """
SELECT rooms.name AS room_name, COUNT(DISTINCT messages.user_id) AS user_count
FROM messages
JOIN rooms ON messages.room_id = rooms.id
GROUP BY rooms.name;
"""
cur.execute(query)
results = cur.fetchall()

print("Počet různých uživatelů, kteří poslali zprávy do jednotlivých místností:")
for row in results:
    print(f"Místnost: {row[0]}, Počet uživatelů: {row[1]}")

conn.close()


print()

#Task 3: Nájsť miestnosti, do ktorých konkrétny používateľ (napr. user2) poslal správy.


conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()


query = """
SELECT DISTINCT rooms.name AS room_name
FROM messages
JOIN rooms ON messages.room_id = rooms.id
JOIN users ON messages.user_id = users.id
WHERE users.username = 'user2';
"""
cur.execute(query)
results = cur.fetchall()


print("Místnosti, do kterých user2 poslal zprávy:")
for row in results:
    print(row[0])

conn.close()


print()

#Task 4: Zobraziť počet správ, ktoré poslal každý používateľ.


conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()

query = """
SELECT users.username AS user_name, COUNT(messages.id) AS message_count
FROM messages
JOIN users ON messages.user_id = users.id
GROUP BY users.username;
"""
cur.execute(query)
results = cur.fetchall()

print("Počet zpráv, které poslal každý uživatel:")
for row in results:
    print(f"Uživatel: {row[0]}, Počet zpráv: {row[1]}")

conn.close()

print()

#Task 5: Zobraziť zoznam miestností spolu s počtom správ, ktoré poslali jednotliví používatelia.


conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()


query = """
SELECT rooms.name AS room_name, users.username AS user_name, COUNT(messages.id) AS message_count
FROM messages
JOIN rooms ON messages.room_id = rooms.id
JOIN users ON messages.user_id = users.id
GROUP BY rooms.name, users.username
ORDER BY rooms.name, users.username;
"""
cur.execute(query)
results = cur.fetchall()


print("Seznam místností spolu s počtem zpráv od jednotlivých uživatelů:")
for row in results:
    print(f"Místnost: {row[0]}, Uživatel: {row[1]}, Počet zpráv: {row[2]}")

conn.close()
