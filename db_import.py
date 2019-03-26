import sqlite3
from collections import namedtuple


DEFAULT_DB_FILENAME = 'stage.sqlite3'


def create_db_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def _namedtuple_factory(cursor, row):
    fields = [col[0] for col in cursor.description]
    Row = namedtuple('Row', fields)
    return Row(*row)


if __name__ == '__main__':
    conn = create_db_connection(DEFAULT_DB_FILENAME)
    conn.row_factory = _namedtuple_factory

    c = conn.cursor()
    for row in c.execute('select * from stage'):
        print(f'IMPORTED DATA {row.KOLUMNA_1} {row.KOLUMNA_2}')


