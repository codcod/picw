# Processing data from XLS files via database

Sometimes it is useful/quickest to export data from XLS to a database and take
them from there.

Save XLS file as `CSV UTF-8 (comma separated)` and then:

    (.venv) R:\picw> sqlite3 stage.sqlite3
    sqlite> .sep ;
    sqlite> .import extras/data_to_import.csv STAGE
    sqlite> .q
    (.venv) R:\picw> python src\process_data_from_db.py -d stage.sqlite3


In case of `sqlite3.OperationalError ("Could not decode to UTF-8 column ...")`, install [iconv](http://gnuwin32.sourceforge.net/packages/libiconv.htm) and then convert the file before importing:

    (.venv) R:\picw> set PATH=%PATH%;c:\Program Files (x86)\GnuWin32\bin\
    (.venv) R:\picw> iconv -t utf-8 test_data.csv > test_data_utf8.csvi

