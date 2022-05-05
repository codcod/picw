@echo off
@rem Make Python's virtual enviroment in current directory and install
@rem libraries from the requirements.txt file if it is there.

@echo [INFO] Creating the environment, it might take a while...
python -m venv .venv

@echo [INFO] Switching to the environment...
call .venv\Scripts\activate.bat
@echo|set /p="[INFO] Python executable is "
python -c "import sys; print(sys.executable)"

@echo [INFO] Updating pip
python -m pip install --upgrade pip setuptools

if exist "requirements.txt" (
	@echo [INFO] Installing requirements...
	pip install -r requirements.txt
) else (
	@echo [INFO] No requirements to install ^(missing requirements.txt^), skipping.
)

@echo [INFO] Remember to 'deactivate' when you are done.
