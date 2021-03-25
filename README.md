# instawork
Install mysql, python on local machine

Create pthon env `python -m venv env`

install all requirements `pip install -r requirements.txt`

For db schema: `python manage.py migrate`. it will create db schema in mysql db

run server `python manage.py runserver`

open browser to see `localhost:8000/team/` to see all team data `curl --location --request GET 'localhost:8000/team'`

Create new data `curl --location --request POST 'localhost:8000/team/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "suru",
    "last_name": "p",
    "email": "sdhbj@jdfhkj.sdh",
    "mobile": "9598523647",
    "role": "ADMIN"
}'`

update any data `curl --location --request PATCH 'localhost:8000/team/587e6f53-b9e9-4493-9a5b-4f72fc9ee62e/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "raju2"
}'`

Delete data `curl --location --request DELETE 'localhost:8000/team/587e6f53-b9e9-4493-9a5b-4f72fc9ee62e/'`

where UUID is unique id for for team member
