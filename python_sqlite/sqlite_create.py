import contextlib
import sqlite3


def main():

    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute(
        """
                    CREATE TABLE IF NOT EXISTS Movies
                    (Title TEXT, Director TEXT, Year INT)
                    """
    )
    connection.commit()
    connection.close()

    # Using a context manager
    with contextlib.closing(sqlite3.connect('movies.db')) as connection:
        with connection as cursor:
            query = 'SELECT 1,SQLITE_VERSION()'
            print(cursor.execute(query).fetchone())


if __name__ == "__main__":
    main()
