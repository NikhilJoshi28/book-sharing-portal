import gc
from dbconnect import connection
c, conn = connection()
BOOK_DETAILS = []
REQUESTS = []
DETAILS = []

def execute_query(sqlQ):
    BOOK_DETAILS = []
    c.execute(sqlQ)
    data = c.fetchall()
    for row in data:
        book = [row[1], row[2], row[3], row[4], row[5], row[0]]
        BOOK_DETAILS.append(book)
    conn.commit()
    gc.collect()

    return BOOK_DETAILS

def execute_id(sqlQ):
    REQUESTS = []
    c.execute(sqlQ)
    data = c.fetchall()
    for row in data:
        request = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
        REQUESTS.append(request)
    conn.commit()
    gc.collect()

    return REQUESTS

def executeUser_id(sqlQ):
    DETAILS = []
    c.execute(sqlQ)
    data = c.fetchall()
    for row in data:
        detail = [row[0], row[1], row[2], row[3], row[4]]
        DETAILS.append(detail)
    conn.commit()
    gc.collect()


def Content():
    sqlQ = "select * from bookdetails order by bookname asc"
    return execute_query(sqlQ)

def searchContent(query):
    sqlQ = "select * from bookdetails where bookname LIKE '%" + str(query) + "%' order by bookname asc"
    return execute_query(sqlQ)

def searchByID(query):
    sqlQ = "select * from bookdetails where userID = '" + str(query) + "' order by bookname asc"
    return execute_query(sqlQ)

def requestsByLender(id):
    sqlQ = "select * from requests where lenderID = '" + str(id) + "' order by startDate asc"
    return execute_id(sqlQ)

def requestsByBorrower(id):
    sqlQ = "select * from requests where borrowerID = '" + str(id) + "' order by startDate asc"
    return execute_id(sqlQ)

def approveR(id):
    sqlQ = "update requests set approvalStatus = 1 where requestID = '" + str(id) + "'"
    c.execute(sqlQ)
    print "executed"
    conn.commit()
    gc.collect()

def getUserSQL(id):
    sqlQ = ""
    return executeUser_id(sqlQ)

def getDate():
    sqlQ = "Date()"
    c.execute(sqlQ)
    date = (c.fetchone())[0]
    conn.commit()
    gc.collect()
    return date