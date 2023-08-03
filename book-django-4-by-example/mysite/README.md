# Project mysite from book Django 4 By Example

1. Creat a project
    - `mkdir mysite`
    - `poetry init`
    - `poetry install --no-root`
2. Set up the project
    - `poetry shell`
    - `django-admin startproject mysite .`
    - `python manage.py runserver`
3. Add blog models
   - `python manage.py makemigrations blog`
   - `python manage.py sqlmigrate blog 0001`
   - `python manage.py migrate`
