import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "mysqlpass",
                           db = "booksharing")
    c = conn.cursor()
    print('hello')
    return c, conn