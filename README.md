## CallerAPI


## How to Run Code Base

-  make python3 virtual venv
-  pip install requirements.txt
-  python manage.py makemigrations
-  python manage.py migrate

-  python manage.py runserver


# API endpoints
- api/register/     -> POST, register new user (with phone, email password)
- api/global_entry/ -> POST, create global user entry with phone and name
- api/global_entry/ -> GET,  search user with name and phone in entire global data base
- api/login/        -> POST, login and get auth Token
- api/mark_spam/    -> POST, mark user phone number spam

