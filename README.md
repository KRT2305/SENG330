# project-team-4

## To get the server running:
- pull and cd into project-team-4/Project/car_share/
- type python3 manage.py makemigrations
- type python3 manage.py migrate
- type python3 manage.py runserver
- visit 127.0.0.1:8000/auto to begin signup

## to set customer hours:
- go to 127.0.0.1:8000/admin and login
- username: admin
 - password: getthemoney
- click on the customer under "Users"
- set the last name field to the number of hours to allocate

*note: when creating bookings, depot must match the vehicle it is assigned to in admin

 ## FILES
 ### models.py
 contains base classes
 ### managers.py
 Wrapper on base classes, used for interacting with the models
 ### querysets.py
 Where queries from managers.py interacte with the db
 ### test.py
 Contains simple scripts for generating users and testing manager.py logic with the database
 ### globals.py
 Contains constants which can be imported elsewhere in the code
 ### views.py
 Contains logic for interacting with user requests
 ### urls.py
 Links urls to views
 ### forms.py
 Describes the page set up and retrieves user filled information
 ### admin.py
 Links classes to the built in django admin page
