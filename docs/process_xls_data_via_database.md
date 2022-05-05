# Process data from XLS files via database

Workflow is the following:

1. Export data from XLS to CSV ("save as").
1. Import CSV to SQLite.
1. Process data (SQL, Python).
1. Export data from database back to Excel (CSV).

Because sometimes it is useful/quickest to export data from XLS to a database
and take them from there.

Save XLS file as `CSV UTF-8 (comma separated)` and then:

    (.venv) R:\picw> sqlite3 stage.sqlite3
    sqlite> .sep ;
    sqlite> .import --csv --skip 1 extras/data_to_import.csv STAGE
    sqlite> .q

Data is imported into the local database, it's time to process it:

    (.venv) R:\picw> python picw\process_data_from_db.py -d stage.sqlite3


In case of `sqlite3.OperationalError ("Could not decode to UTF-8 column ...")`,
install [iconv](http://gnuwin32.sourceforge.net/packages/libiconv.htm) and then
convert the CSV file before importing:

    (.venv) R:\picw> set PATH=%PATH%;c:\Program Files (x86)\GnuWin32\bin\
    (.venv) R:\picw> iconv -t utf-8 test_data.csv > test_data_utf8.csv

## Export to Excel

Use `.excel` dot-command to quickly export to temporary CSV and open in the
default editor:

    sqlite> .excel
    sqlite> select * from table_to_export;

