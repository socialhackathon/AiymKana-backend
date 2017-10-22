# AiymKana Backend

The backend part of the AiymKana application aimed to provide useful information and help regarding the violence for the vulnerable social groups 

It provides the data for the mobile app through the Django REST Framework API

Prerequisites
-------------

- Python >= 3.6
- pip

Required packages:

* Django 1.11.6
* djangorestframework

Usage
-----

- Clone the repository

        git clone https://github.com/socialhackathon/AiymKana-backend.git

- Install dependencies

    Pipenv locates the Pipfile, create a new virtual environment and install the necessary packages.

        pip install pipenv
        pipenv install
        
    Alternatively, the <code>virtualenv</code> can be used
    In that case the required packages can be installed manually

- Migrate the data to the database
    The default database used is sqlite, it can be changed in akana/settings.py file
    
        pipenv run python manage.py makemigrations
        pipenv run python manage.py migrate
        # creates the tables in the database 
    
        pipenv run python manage.py createsuperuser
        # creates profile for admin page with superuser privilegies

        pipenv run python manage.py runserver
        
By default the development server runs at <code>127.0.0.1:8000</code>