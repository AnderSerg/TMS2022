import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Nokia5230",
    database="test_db"
)

# cursor = db.cursor()
# cursor.execute("CREATE TABLE salesman (name VARCHAR(255), user_name VARCHAR(255))")

cursor = db.cursor()

# sql = "DROP TABLE orders"
#
# cursor.execute(sql)

# cursor.execute("""CREATE TABLE orders (ord_no INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                                     purch_amt FLOAT,
#                                     ord_date VARCHAR(255),
#                                     customer_id INT(11),
#                                     salesman_id INT(11))""")

cursor.execute("DESC orders")
print(cursor.fetchall())

# query = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
# values = [
#     (70001, 150.5, '2012-10-05', 3005, 5002),
#     (70009, 270.65, '2012-09-10', 3001, 5005),
#     (70002, 65.26, '2012-10-05', 3002, 5001),
#     (70004, 110.5, '2012-08-17', 3009, 5003),
#     (70007, 948.5, '2012-09-10', 3005, 5002),
#     (70005, 2400.6, '2012-07-27', 3007, 5001),
#     (70008, 5760, '2012-09-10', 3002, 5001),
#     (70010, 1983.43, '2012-10-10', 3004, 5006),
#     (70003, 2480.4, '2012-10-10', 3009, 5003),
#     (70012, 250.45, '2012-06-27', 3008, 5002),
#     (70011, 75.29, '2012-08-17', 3003, 5007),
#     (70013, 3045.6, '2012-04-25', 3002, 5001)
# ]

# cursor.executemany(query, values)
# db.commit()
# print(cursor.rowcount, "records inserted")

query = "SELECT * FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007"
cursor.execute(query)
print(cursor.fetchall())

db.close()
