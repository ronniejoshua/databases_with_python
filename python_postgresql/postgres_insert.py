import psycopg2
from credentials import postgres_red30


conn = psycopg2.connect(**postgres_red30)

cursor = conn.cursor()

cursor.execute("""
                INSERT INTO SALES(ORDER_NUM, 
                ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, 
                QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
                    (
                    1105910, 'Retail', 'Syman Mapstone', 'EB521', 
                    'Understanding Artificial Intelligence', 3,
                    19.5, 0, 58.5
                    )
                """)

conn.commit()

# Query Data
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
for row in rows:
    print("CUST_NAME =", row[0])
    print("ORDER_TOTAL=", row[1], "\n")

conn.close()
