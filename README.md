# Python in Corporate Windows

Once in a while I have to quickly set up a simple Python script in corporate
environment. Since I'm not that familiar with Windows here are notes to help
me navigate the most common quirks (hegemony of XLSX files and ISO-8859-2
encoding) to try and speed up the process.


## Dev workspace

    C:\> mkdir %USERPROFILE%\PROJECTS
    C:\> subst r: %USERPROFILE%\PROJECTS       % requires redo after reboot
    C:\> R:
    R:\> git clone https://github.com/codcod/picw.git
    R:\> cd picw
    R:\picw> scripts/make_venv_here.bat


## Tips

- [Processing XLS data using a staging database](docs/process_xls_data_via_database.md)


## Links


1. [Python](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
1. [SQLite](https://sqlite.org/download.html)
1. [SQLiteBrowser](https://sqlitebrowser.org/dl/)
1. [VSCode](https://vscode-update.azurewebsites.net/latest/win32-x64-user/stable)
1. [Mu](https://codewith.mu/en/download)
1. [Notepad++](https://notepad-plus-plus.org/downloads/v8.4/)
1. [Neovim](https://github.com/neovim/neovim/releases/)

