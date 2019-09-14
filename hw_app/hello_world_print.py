import typing
import os
import psycopg2


def get_db_word():
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        #conn = psycopg2.connect(dbname='helloworlddb8', user='postgres', host='localhost')
    except Exception:
        return 'ERROR (con)'

    try:
        cursor = conn.cursor()
    except Exception:
        conn.close()
        return 'ERROR (cursor)'

    try:
        cursor.execute('SELECT * FROM words limit 1')
    except Exception:
        cursor.close()
        conn.close()
        return 'ERROR (select)'

    record = cursor.fetchone()
    cursor.close()
    conn.close()

    if isinstance(record, typing.Tuple) and len(record) == 2:
        return record[1]
    else:
        return 'ERROR (row type)'


def get_just_word():
    return 'hello'


def get_phrase():
    return get_just_word() + ' ' + get_db_word()


if __name__ == "__main__":
    print(get_phrase())
