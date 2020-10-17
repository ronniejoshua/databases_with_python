import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from credentials import mysql_household


engine = db.create_engine(mysql_household, echo=True)

# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.declarative_base
# declarative_base() is a factory function that constructs a base class for declarative class definitions
Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema': 'household'}

    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))
    description = db.Column(db.String(length=50))

    def __repr__(self):
        return "<Project(title'{0}', description='{1})'>".format(
            self.title, self.description)


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'household'}

    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('household.projects.project_id'))
    description = db.Column(db.String(length=50))

    # Establishes the foreign key relationship
    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0})'>".format(self.description)


Base.metadata.create_all(engine)
