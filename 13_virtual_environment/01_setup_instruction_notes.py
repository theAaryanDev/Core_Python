#Lecture 24 : Python Virtual Environment Guide

# pip/pip3 install virtualenv | link → https://pypi.org/project/virtualenv/
# Docs : https://github.com/pypa/virtualenv | https://virtualenv.pypa.io/en/latest/ | https://docs.python.org/3/library/venv.html

# Steps/Commands to setup/install virtual environment: 
# pip3 install virtualenv (one-time-run)
# go to directory where you want to create virtualenv
# python -m venv .venv | NOTE: .venv is directory name that you choose | syntax → python/python3 -m venv <your_path> 

# Steps/Commands to activate virtual environment:
# to activate → .\.venv\Scripts\Activate.ps1 | Synatax → .\<env_name>\Scripts\Activate.ps1
# Syntax Recommended by VS Code → & c:\Aryan\TheAryanDev\Python\.venv\Scripts\Activate.ps1 | just for reference, Do NOT use this, may throw err.
# to deactivate →  deactivate
# to verify → which python
# Terminal should show the name of your virtual environment in brackets (eg. (.venv) PS C:\Aryan\TheAryanDev\Python>) | if it shows that, then you are in virtual environment
# Terminal automatically switches to the virtual environment when you open it in VS Code (if you have already created virtual environment in that directory) | if it doesn't switch automatically, then click on the python version shown at the bottom left corner of VS Code and select the python interpreter from your virtual environment (eg. .venv\Scripts\python.exe)

# to check how many total packages are installed on your python venv? → pip list
# to export/overwrite all installed packages into a txt file → pip list > requirement.txt
# to install dependencies/ all packages → pip install -r ./requirements.txt
# to install any package in .venv → pip install pymongo
# to unistall any package in .venv → pip unistall pymongo