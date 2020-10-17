import psycopg2
from credentials import postgres_red30


def insert_sale(connection, order_num, order_type, cust_name, prod_number,
                prod_name, quantity, price, discount):
    """
    """
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount

    sale_data = (order_num, order_type, cust_name, prod_number, prod_name,
                 quantity, price, discount, order_total)

    cur = connection.cursor()
    cur.execute('''DELETE FROM SALES WHERE ORDER_NUM=1105910''')
    cur.execute('''
                    INSERT INTO SALES(
                    ORDER_NUM, ORDER_TYPE, CUST_NAME,PROD_NUMBER, PROD_NAME, 
                    QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                sale_data)
    connection.commit()

    cur.execute('''SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=%s;''', (order_num,))

    rows = cur.fetchall()
    for row in rows:
        print("CUST_NAME = ", row[0])
        print("ORDER_TOTAL = ", row[1], "\n")


if __name__ == '__main__':
    connection = psycopg2.connect(**postgres_red30)
    order_num = int(input("What is the order number?\n"))
    order_type = input("What is the order type: Retail or Wholesale?\n")
    cust_name = input("What is the customer's name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("How many were bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))

    insert_sale(connection, order_num, order_type, cust_name, prod_number, prod_name,
                quantity, price, discount)

    print("Data inserted!")

    connection.close()
