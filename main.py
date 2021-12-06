import psycopg2
DB_HOST="jdbc:postgresql://localhost:5432/majorproject"
DB_NAME="majorproject"
DB_USER="sourav_postgres"
DB_PASS="sourav1234"

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database="majorproject",
        user="sourav_postgres",
        password="sourav1234")
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    conn.close()
