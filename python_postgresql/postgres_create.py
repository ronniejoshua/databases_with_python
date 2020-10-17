import psycopg2
from credentials import postgres_red30


def main():
    connection = psycopg2.connect(**postgres_red30)
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS  Sales
                    (ORDER_NUM INT PRIMARY KEY,
                        ORDER_TYPE TEXT,
                        CUST_NAME TEXT,
                        PROD_NUMBER TEXT,
                        PROD_NAME TEXT,
                        QUANTITY INT,
                        PRICE REAL,
                        DISCOUNT REAL,
                        ORDER_TOTAL REAL);
                ''')
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
