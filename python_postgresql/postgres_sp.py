import psycopg2
from credentials import postgres_red30, postgres_red30_orm
from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
CREATE OR REPLACE
PROCEDURE return_nondiscounted_item(INT, INT) 
LANGUAGE plpgsql AS $$ BEGIN

UPDATE
    sales
SET
    quantity = quantity - $2,
    order_total = order_total - (price * $2)
WHERE
    order_num = $1
    AND discount = 0;
COMMIT;
END;
$$;
"""

if __name__ == "__main__":

    # Method 1
    connection = psycopg2.connect(**postgres_red30)
    # https://www.psycopg.org/docs/connection.html#connection.autocommit
    connection.autocommit = True
    cursor = connection.cursor()

    # Calling store procedure
    # In other words, stored procedures are a way to group a set of SQL statements that you
    # may want to reuse for a given piece of functionality in the future. Using stored
    # procedures can help improve your databases performance.
    cursor.execute('''CALL return_nondiscounted_item(%s, %s)''', (1100934, 1))

    # How to Call Postgres Function?
    # https://www.psycopg.org/docs/cursor.html#cursor.callproc
    # cursor.callproc('return_nondiscounted_item', (1100934, 1))
    connection.close()

    # Using SQLAlchemy Core
    engine = create_engine(postgres_red30_orm, isolation_level="AUTOCOMMIT")
    with engine.connect() as connection:
        meta = MetaData(engine)
        sales_table = Table('sales', meta, autoload=True, autoload_with=engine)

        # If autocommit/isolation_level is true then comment out the following
        # connection.execute('COMMIT')

        connection.execute('CALL return_nondiscounted_item (%s, %s)', (1100934, 1))

    # Using SQLAlchemy ORM
    engine = create_engine(postgres_red30_orm)
    Base = declarative_base(engine)
    Base.metadata.reflect(engine)


    class Sales(Base):
        __table__ = Base.metadata.tables['sales']

        def __repr__(self):
            return '''<Sale(order_num='{0}', order_type='{1}',
                        cust_name='{2}',prod_name='{3}', quantity='{4}',
                        order_total='{5}'>'''.format(self.order_num,
                                                     self.order_type,
                                                     self.cust_name,
                                                     self.prod_name,
                                                     self.quantity,
                                                     self.order_total)

    with engine.connect() as connection:
        connection.execute("COMMIT")
        connection.execute('CALL return_nondiscounted_item (%s, %s)', (1100934, 1))
