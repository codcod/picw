"""Connect to local database and process data."""
# pylint: disable=invalid-name,redefined-outer-name

import argparse
import os
import sqlite3
from collections import namedtuple

DEFAULT_DB_FILENAME: str = 'staging.sqlite'


def create_db_connection(db_file: str):
    """Connect to database with file name and return cursor."""
    if os.path.isfile(db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None
    raise FileNotFoundError(f'Database file missing: {db_file}')


def _namedtuple_factory(cursor: sqlite3.Cursor, row: sqlite3.Row):
    fields = [col[0] for col in cursor.description]
    Row = namedtuple('Row', fields)  # type: ignore
    return Row(*row)


parser = argparse.ArgumentParser()
parser.add_argument(
    '-d',
    '--database',
    default=DEFAULT_DB_FILENAME,
    help='SQLite database to read from',
)
args = parser.parse_args()

db_file = args.database

conn = create_db_connection(db_file)
conn.row_factory = _namedtuple_factory

c = conn.cursor()
for row in c.execute('select * from stage'):
    print(f'IMPORTED DATA: {row.KOLUMNA_1} {row.KOLUMNA_2}')

# vim: sw=4:et:ai
