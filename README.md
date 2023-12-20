# Django Forum

A simple forum site built with Django and a little bit of HTMX.

## Screenshots

![A screenshot of the home page](https://github.com/RikuPutkinen/django-forum/blob/main/screenshots/index.png?raw=true)

![A screenshot of the board page](https://github.com/RikuPutkinen/django-forum/blob/main/screenshots/board.png?raw=true)

![A screenshot of the post page](https://github.com/RikuPutkinen/django-forum/blob/main/screenshots/post.png?raw=true)

## Installation

```
git clone git@github.com:RikuPutkinen/django-forum.git
cd django-forum/
python3.11 -m venv .venv
source .venv/bin/activate
python3.11 -m pip install -r requirements.txt 
python3.11 mainsite/manage.py migrate
python3.11 mainsite/manage.py createsuperuser

# Input the credentials for the admin user here

python3.11 mainsite/manage.py runserver
```

After this login to the admin page (eg. http://127.0.0.1:8000/admin) and create the boards.