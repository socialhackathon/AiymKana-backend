# AiymKana Backend

=======================

This project is done using the Django Framework

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

Clone the repository

.. code-block:: bash

    git clone https://github.com/socialhackathon/AiymKana-backend.git

Install dependencies

Pipenv locates the Pipfile, create a new virtual environment and install the necessary packages.

.. code-block:: bash

    pip install pipenv
	pipenv install


Migrate the data to the database
The default database used is sqlite

.. code-block:: bash

    pipenv run python manage.py migrate
    # creates the tables in the database specified in settings.py file
    
    pipenv run python manage.py createsuperuser
    # creates profile for admin page with superuser privilegies
    
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
    pipenv run python manage.py runserver


