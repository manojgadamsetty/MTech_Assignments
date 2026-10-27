import sqlite3
import sys


BITS_ID = sys.argv[1]
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
conn.executemany("INSERT INTO users (name, email) VALUES (?, ?)", [
    ("Asha", "asha@lab.test"),
    ("Ravi", "ravi@lab.test"),
    ("Meena", "meena@lab.test"),
    ("Kiran", "kiran@lab.test"),
    ("Arun", "arun@lab.test"),
    (BITS_ID, BITS_ID.lower() + "@lab.test"),
])


def find_user(email, sort):
    sort_columns = {"NAME": "name", "EMAIL": "email"}
    column = sort_columns.get(sort.upper())
    if column is None:
        raise ValueError("Sort must be NAME or EMAIL.")
    sql = f"SELECT id, name, email FROM users WHERE email = ? ORDER BY {column} LIMIT 10"
    print("SQL:", sql)
    return conn.execute(sql, (email,)).fetchall()


print(BITS_ID)
print("valid:", find_user(BITS_ID.lower() + "@lab.test", "NAME"))
print("injection:", find_user("' OR '1'='1' --", "NAME"))
try:
    find_user(BITS_ID.lower() + "@lab.test", "name; DROP TABLE users")
except ValueError as error:
    print("bad sort rejected:", error)
print("row count:", conn.execute("SELECT COUNT(*) FROM users").fetchone()[0])
