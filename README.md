# AiymKana Backend

The backend part of the AiymKana application aimed to provide useful information and help regarding the violence for the vulnerable social groups 

Features
---------

Installed apps:

* Django 1.11+
* mysqlclient
* djangorestframework

Prerequisites
-------------

- Python >= 3.6
- pip

Usage
-----

- Clone the repository

        git clone https://github.com/socialhackathon/AiymKana-backend.git

- Install dependencies

    Pipenv locates the Pipfile, create a new virtual environment and install the necessary packages.

        pip install pipenv
        pipenv install

- Migrate the data to the database
    The default database used is sqlite, it can be changed in akana/settings.py file

        pipenv run python manage.py migrate
        # creates the tables in the database 
    
        pipenv run python manage.py createsuperuser
        # creates profile for admin page with superuser privilegies
    
        pipenv run python manage.py makemigrations
        pipenv run python manage.py migrate
        pipenv run python manage.py runserver