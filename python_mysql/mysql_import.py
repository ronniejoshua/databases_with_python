import mysql.connector as mysql
import csv
from credentials import mysql_sales_credentials

connection = mysql.connect(**mysql_sales_credentials)

cursor = connection.cursor()

# Method 1: Creating and Inserting data
create_query = '''CREATE TABLE salesperson1(
            id INT(255) NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email_address VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            state VARCHAR(255) NOT NULL,
            PRIMARY KEY (id))'''

cursor.execute("DROP TABLE IF EXISTS salesperson1")
cursor.execute(create_query)

with open('./salespeople.csv', 'r') as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        row_tuple = tuple(row)
        cursor.execute(
            'INSERT INTO salesperson1(first_name, last_name, email_address, city, state) VALUES("%s", "%s", "%s", '
            '"%s","%s")',
            row_tuple)

# Method 2: Creating and Inserting data
create_query = '''CREATE TABLE salesperson2(
            id INT(255) NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email_address VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            state VARCHAR(255) NOT NULL,
            PRIMARY KEY (id))'''

cursor.execute("DROP TABLE IF EXISTS salesperson2")
cursor.execute(create_query)

q = '''LOAD DATA LOCAL INFILE 
    '/Users/ronniejoshua/Downloads/databases_with_python/python_mysql/salespeople.csv'
     INTO TABLE salesperson2 FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
     (first_name, last_name, email_address, city, state);'''

cursor.execute(q)
connection.commit()

cursor.execute("SELECT * FROM salesperson1 LIMIT 2")
print(cursor.fetchall())

cursor.execute("SELECT * FROM salesperson2 LIMIT 2")
print(cursor.fetchall())

connection.close()
