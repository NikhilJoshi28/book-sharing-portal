import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "mysqlpass",
                           db = "booksharing")
    c = conn.cursor()
    print('MySQL database connected')
    return c, conn