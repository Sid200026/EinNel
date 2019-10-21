## EXPOund Hackathon : An employee perfomance review system

Clone this repository in a folder and change your directory to that folder

### Contribution

All contributions to this repository are welcome. However all contributors must follow the CONTRIBUTING.md before submitting any pull requests.

Also contributors must raise an issue before submitting a Pull Request

### Requisites

`pip install -r requirements.txt`

Then we need to create the database for the project. To do that use

`cd EinNell && python3 manage.py makemigrations`

`python3 manage.py migrate`

Now the final thing to do is create a superuser

`python3 manage.py createsuperuser`

On doing this you will be prompted through a series of steps
On completion you will get a message 
`Superuser created successfully.`

Now we are done

To run this on your local machine

`python3 manage.py runserver`

### Features

2 types of users are there
#### 1. Employee
#### 2. Authority

Login Page for both employee and authorities, however signup page is only for employees

#### Employees

1. Can see their to do list of tasks and complete them
2. Can see their head details ( Name, phone, mail)
3. Can send mail to superiors
4. Can edit their personal details ( Only once )
5. Can chat with their senior and other employees under that senior

#### Authorities

1. Can create and assign tasks to employees
2. Rate Tasks
3. Can see all the completed tasks
4. Contact employees
5. Promote employees to authority position
6. Review employee perfomance
7. Chat with their employees

### Team Members
1. -[@ananya2407](https://github.com/ananya2407)
2. -[@soumyadeeptadas](https://github.com/soumyadeeptadas)
3. -[@Sid200026](https://github.com/Sid200026)
