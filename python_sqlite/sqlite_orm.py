import sqlalchemy as db

if __name__ == "__main__":

    # Creating a database engine and connecting to it
    engine = db.create_engine('sqlite:///movies.db')
    connection = engine.connect()

    # Creating an access to a table in the database
    metadata = db.MetaData()
    movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

    # Querying the database table
    query = db.select([movies])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    print(result_set[0])
    print(result_set[:2])

    # Querying the database table - Using where clause
    query = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    print(result_set[0])

    # Inserting records in the database table
    query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year="1960")
    connection.execute(query)

    # Querying the table
    query = db.select([movies])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    print(result_set)
