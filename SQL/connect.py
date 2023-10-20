import pymysql

def query_user(userid):
    connect = pymysql.Connect(
        host='124.222.3.109',
        port=3306,
        user='root',
        passwd='1e561ve65a1vwe65f1e65waveq',
        db='default',
        charset='utf8'
    )
    cursor = connect.cursor()
    sql = "SELECT cid, password ,rating FROM `default_member` WHERE cid LIKE %s"
    cursor.execute(sql, (f'%{userid}%',))
    result = cursor.fetchone()
    return result