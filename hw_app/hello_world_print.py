import typing
import psycopg2


def get_db_word():
    try:
        conn = psycopg2.connect(dbname='hello_world_db', user='postgres', host='localhost')
    except Exception:
        return 'ERROR'

    try:
        cursor = conn.cursor()
    except Exception:
        conn.close()
        return 'ERROR'

    try:
        cursor.execute('SELECT * FROM words limit 1')
    except Exception:
        cursor.close()
        conn.close()
        return 'ERROR'

    record = cursor.fetchone()
    cursor.close()
    conn.close()

    if isinstance(record, typing.Tuple) and len(record) == 2:
        return record[1]
    else:
        return 'ERROR'


def get_just_word():
    return 'hello'


def get_phrase():
    return get_just_word() + ' ' + get_db_word()


if __name__ == "__main__":
    print(get_phrase())
