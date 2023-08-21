# Thesis project / Django app

Internal repository for the "Ewallet" Django app project with Mysql db integration using liquibase. Python 3.10.

Additional connectors:
mysql-connector-python
django-mysql

Recommended: run pipenv for a local environment and use it as your default vscode interpreter.

`pip install pipenv`
`pipenv --python3.10`
`pipenv install django`
`pipenv shell`

Make sure mysql connector data is correct and your liquibase instance is running

/ewallet/ is the base app
subsequent apps (onboarding, transactions, users, auth, etc) will reside inside it.

First time? Make sure you migrate django sessions to the db:  
`python manage.py migrate`

Run the app:

`python manage.py runserver`
