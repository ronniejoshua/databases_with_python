import mysql.connector as mysql
from credentials import mysql_sales_credentials


def connect(db_name):
    try:
        credentials = mysql_sales_credentials.copy()
        credentials['database'] = db_name
        return mysql.connect(**credentials)
    except Exception as e:
        print(e)


def add_new_project(cursor_obj, project_title, project_description, task_descriptions):
    project_data = (project_title, project_description)
    cursor_obj.execute('''INSERT INTO projects(title, description) VALUES (%s, %s)''', project_data)
    project_id = cursor.lastrowid
    tasks_data = []
    for description in task_descriptions:
        task_data = (project_id, description)
        tasks_data.append(task_data)
    cursor.executemany('''INSERT INTO tasks(project_id, description) VALUES (%s, %s)''', tasks_data)


if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_new_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(tasks_records)

    db.close()
