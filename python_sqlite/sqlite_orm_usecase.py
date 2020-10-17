import sqlalchemy as db

engine = db.create_engine('sqlite:///users-sqlalchemy.db')
metadata = db.MetaData()
connection = engine.connect()

# Creating table
users = db.Table('Users', metadata,
                 db.Column('user_id', db.Integer, primary_key=True),
                 db.Column('first_name', db.Text),
                 db.Column('last_name', db.Text),
                 db.Column('email_address', db.Text))
metadata.create_all(engine)

# Inserting Values
insertion_query = users.insert().values([
    {"first_name": "Tina", "last_name": "Mccoy", "email_address": "tmccoyl@hplussport.com"},
    {"first_name": "Joan", "last_name": "Ruiz", "email_address": "jruixm@hplussport.com"},
    {"first_name": "Sara", "last_name": "Cox", "email_address": "scoxn@hplussport.com"},
    {"first_name": "Jessica", "last_name": "Alvarez", "email_address": "jalvarezo@hplussport.com"},
    {"first_name": "Amanda", "last_name": "Butler", "email_address": "abutlerp@hplussport.com"}
])
connection.execute(insertion_query)

# Querying Data
selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)
print(selection_result.fetchall())
