#!"C:\Python35\python.exe"

import MySQLdb
import string
import random

KEY_LEN = 20
KEY_COUNT = 200

def base_str():
    return (string.ascii_letters + string.digits)

def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

def key_num(num, result = None):
    if result is None:
        result = []
    for i in range(num):
        result.append(str(key_gen()))
    return result

class mysql_init(object):

    def __init__(self, conn):
        self.conn = None
    
    #connect to mysql
    def connect(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            password="pass",
            db="testdb",
            charset="utf8"
        )
    
    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()
    
    def commit(self):
        return self.conn.commit()
    
    def close(self):
        return self.conn.close()
    
def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    dbconn.commit();
    QueryData(conn)
    dbconn.close()

def query(sql, conn):
    '''查询sql'''
    conn.execute(sql)
    rows = conn.fetchall()
    return rows

def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS `user_key`")

def CreateTable(conn):
    sql_create = '''CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)

def InsertDatas(conn):
    insert_sql ="INSERT INTO user_key VALUES(%(value)s)"
    key_list=key_num(KEY_COUNT)
    conn.executemany(insert_sql, [dict(value=v) for v in key_list])
    

def DeleteData(conn):
    del_sql = "delete from user_key where id=2"
    conn.execute(del_sql)

def QueryData(conn):
    sql = "select * from user_key"
    rows = query(sql, conn)
    printResults(rows)

def printResults(rows):
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)

if __name__ =="__main__":
    dbconn = mysql_init(None)
    process()
