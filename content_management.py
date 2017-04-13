import gc
from dbconnect import connection
c, conn = connection()

def Content():
    BOOK_DETAILS = []
    c.execute("select * from bookdetails")
    data = c.fetchall()
    for row in data:
        book = [ row[1], row[2], row[3], row[4] ]
        BOOK_DETAILS.append(book)

    conn.commit()
    gc.collect()

    return BOOK_DETAILS

def searchContent(query):
    BOOK_DETAILS = []
    sqlQ = "select * from bookdetails where bookname LIKE '%" + str(query) + "%'"
    c.execute(sqlQ)
    data = c.fetchall()
    for row in data:
        book = [row[1], row[2], row[3], row[4]]
        BOOK_DETAILS.append(book)

    conn.commit()
    gc.collect()
    return BOOK_DETAILS