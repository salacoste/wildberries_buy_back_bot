
import psycopg2

conn = None
try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        user = "postgres",
        password="WW9JUQhP",
        database="buyback_db",
        port = "5433"
    )

    cur = conn.cursor()

    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    print(db_version)

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')