import psycopg2
from config import configuration

def connect():
    """Connection to postgres Database Server"""
    conn=None
    try:
        params=configuration()
        print("Connection to Postgresql database ")
        conn=psycopg2.connect(host=params['host'],
        database=params['database'],
        user=params['user'],
        password=params['password'])
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn

