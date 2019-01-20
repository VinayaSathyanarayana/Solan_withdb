IMPORTANT READ BEFORE PROCEDING
STEPS TO RUN THE APPLICATION:

1.download/clone this repository
2.install mysql, python, pip, django
3.run activate from the env folder to activate the virtual env
4.create a user called 'db_user' with password 'dbpass' in mysql and grant all privilege on a new databases called cisco_students
5.run " python manage.py makemigrations
        python manage.py migrations
        python manage.py createsuperuser
        python manage.py runserver 8080" run hey one by one following any steps shown if required
6.go to http://127.0.0.1:8080/admin
7.Create 3 groups called "Student", "Teachers", "Admin" without the quotes
8.go to users and and add a user to a group you want
9.go to logins on the admin page and click on the add login button, select the user and save
10.go to points and click on add points, select the login you just created and save
11.now you will be able to access all the featues of the website without any problems

