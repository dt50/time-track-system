# Time track system

## About the project

This project was created for organizations with time control system. This project is only for displayed counting times
and auto generated reports.

## Getting Started

### Installation

- Clone the repo `git clone git@github.com:dt50/time-track-system.git`
- Change the current directory to the template `cd time-track-system`
- Create .env `cp src/.env_example src/.env` and insert data about your email server
- Create virtual environment with poetry `poetry install`
- Make migrations `python manage.py migrate`
- Create superuser `python manage.py createsuperuser`
- Start project `python manage.py runserver`

## Technologies used

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" alt="Django Rest Framework"/>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgresSQL"/>