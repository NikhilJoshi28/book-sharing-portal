import gc
from dbconnect import connection
c, conn = connection()
BOOK_DETAILS = []

def execute_query(sqlQ):
    BOOK_DETAILS = []
    c.execute(sqlQ)
    data = c.fetchall()
    for row in data:
        book = [row[1], row[2], row[3], row[4], row[5]]
        BOOK_DETAILS.append(book)
    conn.commit()
    gc.collect()

    return BOOK_DETAILS


def Content():
    sqlQ = "select * from bookdetails"
    return execute_query(sqlQ)

def searchContent(query):
    sqlQ = "select * from bookdetails where bookname LIKE '%" + str(query) + "%'"
    return execute_query(sqlQ)

def searchByID(query):
    sqlQ = "select * from bookdetails where userID = '" + str(query) + "'"
    return execute_query(sqlQ)