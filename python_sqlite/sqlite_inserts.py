import sqlite3

if __name__ == "__main__":
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    # Inserting Records in Database
    cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

    # Inserting Multiple Records
    famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
                   ('Back to the Future', 'Steven Spielberg', 1985),
                   ('Moonrise Kingdom', 'Wes Anderson', 2012)]

    cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)

    # Extracting records from database
    records = cursor.execute("SELECT * FROM Movies")
    for record in records:
        print(record)

    # Extracting records from database
    print(cursor.execute("SELECT * FROM Movies").fetchall())
    print(cursor.execute("SELECT * FROM Movies").fetchone())
    print(cursor.execute("SELECT * FROM Movies").fetchmany(3))

    # Extracting records from database using where clause
    release_year = (1985,)
    print((cursor
           .execute("SELECT * FROM Movies WHERE year=?", release_year)
           .fetchall())
          )

    connection.commit()
    connection.close()
