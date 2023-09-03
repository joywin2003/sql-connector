import mysql.connector

global cnx

cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'dbms'
)

def get_books():
    cur = cnx.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    return rows

def search_book(keyword):
    cur = cnx.cursor()
    sql = "SELECT * FROM books WHERE title LIKE %s"
    keyword_with_wildcards = f"%{keyword}%"
    cur.execute(sql, (keyword_with_wildcards,))
    rows = cur.fetchall()
    return rows

def add_order(order):
    cur = cnx.cursor()
    sql = "INSERT INTO orders (bookID, orderdate, orderamount, userID) VALUES (%s, %s, %s, %s)"
    values = (order['bookID'], order['orderdate'], order['orderamount'], order['userID'])
    cur.execute(sql, values)
    cnx.commit()
    return cur.lastrowid

def remove_order(order_id):
    cur = cnx.cursor()
    sql = "DELETE FROM orders WHERE orderID = %s"
    cur.execute(sql, (order_id,))
    cnx.commit()



