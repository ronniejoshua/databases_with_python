import mysql.connector as mysql
from credentials import mysql_sales_credentials


def connect(db_name):
    try:
        credentials = mysql_sales_credentials.copy()
        credentials['database'] = db_name
        return mysql.connect(**credentials)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    db.close()
