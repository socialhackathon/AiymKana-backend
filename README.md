# AiymKana-backend

This project is done using the Django Framework

The required packages are listed in the Pipfile

# Installation

pip install pipenv

'pipenv install' installs all dependencies

Aimkana Backend
=======================

This project is done using the Django Framework

Features
---------

Installed apps:

* Django 1.11+
* mysqlclient
* djangorestframework

Usage
-----

Create a Django project:

.. code-block:: bash

    mkdir dir_name
    cd dir_name
    django-admin.py startproject hack

Install dependencies

.. code-block:: bash

    pip install pipenv
	pipenv install

Pipenv locates the Pipfiles, create a new virtual environment and install the necessary packages.

Prerequisites
-------------

- Python >= 3.6
- pip
- virtualenv (virtualenvwrapper is recommended)

Installation
------------
	pipenv run ./manage.py migrate
	pipenv run ./manage.py runserver
