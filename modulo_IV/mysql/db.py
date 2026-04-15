import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="python123",
        database="eduit",
        cursorclass=pymysql.cursors.DictCursor
    )
