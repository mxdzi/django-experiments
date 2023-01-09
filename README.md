# My experiments with Django Framework

## Initial setup

1. Add README, gitignore, gitattributes
2. Set python version `pyenv local 3.11`
3. Add virtualenv
   1. `python3 -m venv .venv`
   2. `. .venv/bin/activate`
   3. `pip install --upgrade pip`
   4. `pip install pip-tools`
4. Set python interpreter in PyCharm
5. Add files requirements*.in
   1. `pip-compile`
   2. `pip-compile requirements-dev.in`
   3. Install LIVE `pip-sync`
   4. Install STAGING `pip-sync requirements.txt requirements-dev.txt`
   5. Update all packages `pip-compile --upgrade`
   6. Update selected packages `pip-compile --upgrade-package 'requests<3.0'`

## Projects
### [Django Tutorial](django-tutorial/README.md)
