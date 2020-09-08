# MessageBoard

>just fun

### How to run

- dev-env:
    - change db to your db
    - exec these commands in your terminal
        - cd root dir
        - pip install -r requirements.txt
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py creatsuperuser
        - python manage.py runserver


- release-env:
    - change db to your db
    - exec these commands in your terminal
        - cd root dir
        - modify DEBUG=False and ALLOWED_HOSTS in settings.py
        - pip install -r requirements.txt
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py creatsuperuser
        - python manage.py collectstatic
        - python manage.py runserver
        
- urls:
    - index page：127.0.0.1:8000
    - admin: 127.0.0.1:8000/admin
