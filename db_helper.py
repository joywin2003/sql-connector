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

cur = cnx.cursor()
now = datetime.datetime.now()
datestring  = now.strftime("%Y-%m-%d")

def get_books():
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    return rows

def search_book(keyword):
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
        cur.execute(insert_query, order_data)
        cnx.commit()

        return {"message": "Order added successfully", "order": order}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}


def remove_order(order_id):
    sql_select = "SELECT * FROM orders WHERE orderID = %s"
    sql_delete = "DELETE FROM orders WHERE orderID = %s"
    try:
        cur.execute(sql_select, (order_id,))
        order = cur.fetchone()
        print(order)
        if order is None:
            return {"message": "Order not found"}
        cur.execute(sql_delete, (order_id,))
        cnx.commit()
        return {"message": "Order removed successfully"}
    except Exception as e:
        print(f"Error executing query: {e}")


def get_orders():
    try:
        sql = "SELECT * FROM orders"
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        return {"message": f"Error: {str(e)}"}


remove_order(100)