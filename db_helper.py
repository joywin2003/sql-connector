import mysql.connector
import datetime
from Modal import Orders

global cnx

cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql123',
    database = 'bookstore'
)


now = datetime.datetime.now()
datestring  = now.strftime("%Y-%m-%d")

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

def add_order(order:Orders):
    try:
        insert_query = ("INSERT INTO orders "
                        "(orderID, bookID, orderdate, orderamount, userID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        orderdate_str = order.orderdate.strftime('%Y-%m-%d %H:%M:%S')
        order_data = (order.orderID, order.bookID, orderdate_str, order.orderamount, order.userID)
        cur = cnx.cursor()
        cur.execute(insert_query, order_data)
        cnx.commit()

        return {"message": "Order added successfully", "order": order}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}


def remove_order(order_id):
    cur = cnx.cursor()
    sql = "DELETE FROM orders WHERE orderID = %s"
    try:
        cur.execute(sql, (order_id,))
        cnx.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"Error executing query: {e}")


