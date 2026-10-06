# the-django-show
Tutorial app for customizing the Django admin

This covers
- basic model admin usage
- a model admin custom endpoint example
- a custom admin page example

## Requirements

- python >= 3.14

## Useful commands
```sh
# create a virtual environment and activate it
python -m venv venv
. venv/bin/activate
# install dependencies
pip install --requirement requirements.txt
# run migrations
python showsite/manage.py migrate
# create a django super admin user
python showsite/manage.py createsuperuser
# load data from a neocities website
python showsite/manage.py import-data
# run a local web server at localhost:8000
python showsite/manage.py runserver
```

## Links
- Django Admin source - https://github.com/django/django/tree/main/django/contrib/admin/templates/admin
- Django Getting started - https://www.djangoproject.com/start/