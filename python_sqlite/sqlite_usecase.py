import sqlite3

connection = sqlite3.connect('users-sqlite.db')
cursor = connection.cursor()

# Creating a table
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    first_name TEXT, 
                    last_name TEXT, 
                    email_address TEXT)''')

# Inserting Multiple Records
usersToInsert = [('Tina', 'Mccoy', 'tmccoyl@hplussport.com'),
                 ('Joan', 'Ruiz', 'jruizm@hplussport.com'),
                 ('Sara', 'Cox', 'scozn@hplussport.com'),
                 ('Jessica', 'Alvarez', 'jalvarezo@hplussport.com'),
                 ('Amanda', 'Butler', 'abutlerp@hplussport.com')]

cursor.executemany('''INSERT INTO Users(first_name, last_name, email_address) VALUES (?,?,?)''', usersToInsert)

cursor.execute("SELECT email_address FROM Users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

connection.commit()
connection.close()
