# Tutorial 4.2

## Part 1

1. Start project `django-admin startproject mysite .`
2. Test running server `python manage.py runserver`
3. Add a new app `python manage.py startapp polls`

## Part 2
1. Update settings
2. Run migrations `python manage.py migrate`
3. Create models
4. Make migrations `python manage.py makemigrations polls`
5. Check migrations `python manage.py sqlmigrate polls 0001`
6. Check project `python manage.py check`
7. Create admin user `python manage.py createsuperuser`
