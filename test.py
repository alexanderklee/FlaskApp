import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
print("Len of tuple: ", len(user))

#
# Original code below
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)
# python error - incorrect # of bindings. Workaround is to manually create this test db
#

insert_query = "INSERT INTO users VALUES (1, 'jose', 'asdf')"
cursor.execute(insert_query)
insert_query = "INSERT INTO users VALUES (2, 'Rolf', 'asdf')"
cursor.execute(insert_query)
insert_query = "INSERT INTO users VALUES (3, 'Anne', 'qwer')"
cursor.execute(insert_query)

users = [
    (2, "Rolf", "asdf"),
    (3, "Anne", "qwer")
]

# cursor.execute(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
