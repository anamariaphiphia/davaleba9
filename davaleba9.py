import sqlite3
conn = sqlite3.connect("customers.sqlite")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
result = cursor.execute("SELECT * FROM users")
for row in result:
    print(row["username"],row["phone_number"])
result = cursor.execute("SELECT * FROM users WHERE age > 25")
for row in result:
    print(row["firstname"], row["lastname"], row["age"])

age = 25
resultt = cursor.execute("SELECT * FROM users WHERE age > :age_condition", {"age_condition": age})
for row in resultt:
    print(row["firstname"],row["lastname"],row["age"])
result = cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
for row in result:
    print(row["firstname"],row["lastname"],row["age"])

result = cursor.execute("SELECT * FROM users WHERE age != 20")
for row in result:
    print(row["firstname"],row["lastname"])
cursor.execute("SELECT * FROM users")
rows = cursor.rowcount
result = cursor.execute("SELECT * FROM users WHERE age == 30")
for row in result:
    print(row["firstname"],row["lastname"],row["age"])
result = cursor.execute("SELECT * FROM users WHERE order by age desc")
for row in result:
    print(row["firstname"],row["lastname"],row["age"])

result = cursor.execute("UPDATE users SET username = 'N,astamadze' WHERE age == 20")
for row in result:
    print(row["username"])
result = cursor.execute("DELETE FROM users WHERE user_id == 5 ")
for row in result:
    print(row["user_id"])
result = cursor.execute("DELETE FROM users where firstname like '%a'")
for row in result:
    print(row["firstame"])
conn.commit()



















