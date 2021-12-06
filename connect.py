import psycopg2
from config import configuration

def connect():
    """Connection to postgres Database Server"""
    conn=None
    try:
        params=configuration()
        print("Connection to Postgresql database hekk")
        print(params)
        conn=psycopg2.connect(**params)


        cur=conn.cursor()
        print('PostgreSQL database Version')
        cur.extract('Select Version()')
        db_version=cur.fetchone()
        print(db_version)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database Connection closed")

