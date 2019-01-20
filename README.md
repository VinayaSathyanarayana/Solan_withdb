# Solan_withdb
IMPORTANT READ BEFORE PROCEDING

STEPS TO RUN THE APPLICATION:

-download/clone this repository
-install mysql, python, pip, django
-run activate from the env folder to activate the virtual env
-create a user called 'db_user' with password 'dbpass' in mysql and grant all privilege on a new databases called cisco_students
-run " python manage.py makemigrations
        python manage.py migrations
        python manage.py createsuperuser
        python manage.py runserver 8080" run hey one by one following any steps shown if required
-go to http://127.0.0.1:8080/admin
-Create 3 groups called "Student", "Teachers", "Admin" without the quotes
-go to users and and add a user to a group you want
-go to logins on the admin page and click on the add login button, select the user and save
-go to points and click on add points, select the login you just created and save
-now you will be able to access all the featues of the website without any problems

