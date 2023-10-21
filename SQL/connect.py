import pymysql

def query_user(userid):
    connect = pymysql.Connect(

    )
    cursor = connect.cursor()
    sql = "SELECT cid, password ,rating FROM `default_member` WHERE cid LIKE %s"
    cursor.execute(sql, (f'%{userid}%',))
    result = cursor.fetchone()
    return result