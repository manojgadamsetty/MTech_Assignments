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
    sql = "SELECT id, name, email FROM users WHERE email = '" + email + "' ORDER BY " + sort
    print("SQL:", sql)
    return conn.execute(sql).fetchall()


print(BITS_ID)
print(find_user("ravi@lab.test", "name"))
print(find_user("' OR '1'='1' --", "name"))
