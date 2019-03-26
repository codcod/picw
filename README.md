# HelloWorld

Pierwsze kroki z Py.

## Instalacja

1. [Python](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
1. [VSCode](https://vscode-update.azurewebsites.net/latest/win32-x64-user/stable) lub [Mu](https://codewith.mu/en/download).
1. [SQLiteBrowser](https://sqlitebrowser.org/dl/).


## Œrodowisko

    C:\> mkdir %USERPROFILE%\PROJECTS
    C:\> subst r: %USERPROFILE%\PROJECTS       % po przelogowaniu trzeba
                                               % powtórzyæ to polecenie
    C:\> R:
    R:\> mkdir helloworld
    R:\> cd helloworld
    R:\helloworld> python -m venv venv         % utworzenie wirtualnego
                                               % œrodowiska o nazwie venv
    R:\helloworld> venv\Scripts\activate.bat   % aktywacja witualnego
                                               % œrodowiska
    (venv) R:\helloworld> python -m pip install --upgrade pip  % aktualizacja
                                               % narzêdzia do instalowania
                                               % bibliotek
    (venv) R:\helloworld> pip install ipython  % instalacja lepszego shella ni¿
                                               % zwyk³y python
    (venv) R:\helloworld> ipython              % uruchomienie lepszego shella,
                                               % Ctrl+D to wyjœcie

### Uwagi do œrodowiska

Wirtualne œrodowisko zak³ada siê raz, uruchamia siê wiele razy (skryptem
`activate.bat`). Wyjœcie to polecenie `deactivate` lub po prostu zamkniêcie
wiersza poleceñ. Wirtualne œrodowisko pozwala instalowaæ niezale¿nie wiele
ró¿nych bibliotek. Mo¿na mieæ (i z regu³y siê ma) wiele ró¿nych œrodowisk
wirtualnych.

IPython (trzeba instalowaæ niezale¿nie w ka¿dym œrodowisku wirtualnym). Pomaga
na start, bo ma uzupe³nianie sk³adni i trwa³¹ historiê.

## Ciekawsze biblioteki na start

* `pandas`
* `matplotlib`
* `pendulum`
* `virtualenv`, `virtualenvwrapper` (uzupe³nienie œrodowiska wirtualnego)
* `flake8`, `rope`, `pylint` (do pracy z samym kodem)

## Zaczytywanie danych z CSV

Dane z XLS zapisz jako "CSV UTF-8 (comma separated)". I nastêpnie:

    (venv) R:\helloworld> sqlite3 stage.sqlite3
    sqlite> .sep ;
    sqlite> .import test_data.csv STAGE
    sqlite> .q
    (venv) R:\helloworld> python db_import.py

