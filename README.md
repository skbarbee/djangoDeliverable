## Description

## Routes Table 
| Route| Endpoints |
| --- | --- |
| GET POST | donuts/|
| GET PATCH DELETE | donuts/:pk/ |
| GET POST | stores/|
| GET PATCH DELETE | stores/:pk/ |

## Starting Instructions

- pipenve shell
- pipenv install django==4.1 psycopg2-binary djangorestframework
- django-admin startproject <project_name>
- createdb <db-name>
- cd <project_name>
- python manage.py runserver            


## Helpful CL Commands
- django-admin startapp <app_name>
- python manage.py runserver
- python manage.py make migrations
- python manage.py migrate
- python manage.py showmigrations-