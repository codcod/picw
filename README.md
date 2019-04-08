# HelloWorld

Pierwsze kroki z Py.

## Instalacja

1. [Python](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
1. [VSCode](https://vscode-update.azurewebsites.net/latest/win32-x64-user/stable) lub [Mu](https://codewith.mu/en/download).
1. [SQLiteBrowser](https://sqlitebrowser.org/dl/).


## Środowisko

    C:\> mkdir %USERPROFILE%\PROJECTS
    C:\> subst r: %USERPROFILE%\PROJECTS       % po przelogowaniu trzeba
                                               % powtórzyć to polecenie
    C:\> R:
    R:\> mkdir helloworld
    R:\> cd helloworld
    R:\helloworld> python -m venv venv         % utworzenie wirtualnego
                                               % środowiska o nazwie venv
    R:\helloworld> venv\Scripts\activate.bat   % aktywacja witualnego
                                               % środowiska
    (venv) R:\helloworld> python -m pip install --upgrade pip  % aktualizacja
                                               % narzędzia do instalowania
                                               % bibliotek
    (venv) R:\helloworld> pip install ipython  % instalacja lepszego shella niż
                                               % zwykły python
    (venv) R:\helloworld> ipython              % uruchomienie lepszego shella,
                                               % Ctrl+D to wyjście

### Uwagi do środowiska

Wirtualne środowisko zakłada się raz, uruchamia się wiele razy (skryptem
`activate.bat`). Wyjście to polecenie `deactivate` lub po prostu zamknięcie
wiersza poleceń. Wirtualne środowisko pozwala instalować niezależnie wiele
różnych bibliotek. Można mieć (i z reguły się ma) wiele różnych środowisk
wirtualnych.

IPython (trzeba instalować niezależnie w każdym środowisku wirtualnym). Pomaga
na start, bo ma uzupełnianie składni i trwałą historię.

## Ciekawsze biblioteki na start

* `pandas`
* `matplotlib`
* `pendulum`
* `virtualenv`, `virtualenvwrapper` (uzupełnienie środowiska wirtualnego)
* `flake8`, `rope`, `pylint` (do pracy z samym kodem)

## Zaczytywanie danych z CSV

Dane z XLS zapisz jako "CSV UTF-8 (comma separated)". I następnie:

    (venv) R:\helloworld> sqlite3 stage.sqlite3
    sqlite> .sep ;
    sqlite> .import test_data.csv STAGE
    sqlite> .q
    (venv) R:\helloworld> python db_import.py

Gdy wyskakuje błąd `sqlite3.OperationalError` ("Could not decode to UTF-8 column ..."), to trzeba zainstalować [iconv](http://gnuwin32.sourceforge.net/packages/libiconv.htm) i:

    (venv) R:\helloworld> set PATH=%PATH%;c:\Program Files (x86)\GnuWin32\bin\
    (venv) R:\helloworld> iconv -t utf-8 test_data.csv > test_data_utf8.csv
