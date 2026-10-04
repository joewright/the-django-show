# the-django-show
Tutorial app for customizing the Django admin

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