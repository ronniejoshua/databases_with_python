from sqlalchemy import create_engine
import pandas as pd
from credentials import mysql_sales

# Create and Environment variable
engine = create_engine(mysql_sales, echo=True)

salespeople_df = pd.read_sql_table("salesperson1", con=engine)

specific_salesperson_df = pd.read_sql_table("salesperson1",
                                            con=engine,
                                            index_col='id',
                                            coerce_float=True,
                                            columns=['id', 'city', 'state'],
                                            parse_dates=['dateColumn'],
                                            chunksize=250)

email_df = pd.read_sql("SELECT email_address FROM salesperson1 LIMIT 10", con=engine)
