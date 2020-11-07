import psycopg2


conn = psycopg2.connect(database='club',
            user='postgres',
            password = '9715',
            host='localhost',
            port='5432')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Sales
(
    ORDER_NUM INT PRIMARY KEY,
    CUST_NAME TEXT,
    PROD_NUMBER TEXT,
    PRICE REAL
)

;''')


conn.commit()
conn.close()