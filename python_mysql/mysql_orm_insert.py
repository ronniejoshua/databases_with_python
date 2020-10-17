from sqlalchemy.orm import sessionmaker
from python_mysql.mysql_orm_create import Project, Task, engine


# https://docs.sqlalchemy.org/en/13/orm/session_basics.html
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# Adding/Inserting a record to the database[Adding a Project]
organize_closet_project = Project(title='Organize closet',
                                  description='Organize closet by color and style')
session.add(organize_closet_project)
session.commit()

# Adding/Inserting tasks to the Tasks Table
tasks = [Task(project_id=organize_closet_project.project_id, description='Decide what close to donate'),
         Task(project_id=organize_closet_project.project_id, description='Organize winter clothes'),
         Task(project_id=organize_closet_project.project_id, description="Organize summer clothes")]
session.bulk_save_objects(tasks)
session.commit()

# Querying the the Project(projects table) Object
our_project = session.query(Project).filter_by(title='Organize closet').first()
print(our_project)

# Querying the the Task(tasks table) Object
our_tasks = session.query(Task).all()
print(our_tasks)
