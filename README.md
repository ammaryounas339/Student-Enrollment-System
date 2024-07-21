# Student Enrollment System API Documentation

This documentation outlines the steps to run the REST API for managing student enrollment in courses. The project includes the following key features:

## Features

 - Models for Student, Course, and Enrollment
- REST API endpoints for CRUD operations
- Integration with RabbitMQ and Celery for asynchronous tasks
- Multi-threading for background processing like database backup
- API rate limiting 



## Installation

This API requires [Python](https://www.python.org/) to run.

Set up a virtual environment, Install the dependencies and  start the server.

```sh
python -m venv venv
source venv/Scripts/activate  # On Windows 
```

Install the required packages.

```sh
pip install -r requirements.txt
```
The project is currently using a PostgreSQL database, to connect a PostgreSQL database you need to set up the environment variables for your database and it's better to keep them in a .env file. You can also configure any other database supported by Django.

```sh
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port

```
Apply the database migrations

```sh
python manage.py makemigrations
python manage.py migrate
```
Run the django server

```sh
python manage.py runserver
```

Run the celery worker
```sh
celery -A student_enrollment_system  worker -l info -P gevent   #for Windows only
```
You can also configure your own Email server for sending welcome Emails to students by changing the variables in settings.py
```sh
EMAIL_HOST = 
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD = 
EMAIL_PORT =
```



## API Endpoints
To test our API Endpoints, we can use Postman or navigate to this URL localhost:8000/api/ and as we are using ViewSets which provides us with a similar interface to Postman to test the endpoints. We can also send requests using the terminal with curl to document the endpoints.

### Students
#### List All Students
Endpoint: /api/students/ \
Method: GET \
Description: Retrieves a list of all students\
Request:
```sh
curl -X GET http://127.0.0.1:8000/api/students/
```
Response:
```sh
[
{"id":6,"first_name":"Dajnda","last_name":"scscscs","email":"ahmed@gmail.com","date_of_birth":"2024-07-26"},
{"id":8,"first_name":"Dajndadd","last_name":"scscscsada","email":"axz1709@gmail.com","date_of_birth":"2024-07-26"},
{"id":9,"first_name":"dadadad","last_name":"dadadaqmq","email":"annar@gmail.com","date_of_birth":"2024-07-23"}
]
```
#### Get Single Student by ID
Endpoint: /api/students/{id}/ \
Method: GET\
Description: Retrieves a single student by id\
Request:
```sh
curl -X GET http://127.0.0.1:8000/api/students/15/
```
Response:
```sh
{"id":15,"first_name":"alkanlnssffsffs","last_name":"frwrwrwr","email":"ammaryounas339.ay@gmail.com","date_of_birth":"2024-06-30"}
```
#### Create a new student
Endpoint: /api/students/\
Method: POST\
Description: Create a new student \
Request:
```sh
curl -X POST http://127.0.0.1:8000/api/students/ -H "Content-Type: application/json" -d '{
    "first_name": "Ahmed",
    "last_name": "Sami",
    "email": "ammar@fastmail.com",
    "date_of_birth": "2001-02-02"
}'

```
Response:
```sh
{"id":16,"first_name":"Ahmed","last_name":"Sami","email":"ammar@fastmail.com","date_of_birth":"2001-02-02"}
```
#### Delete a student
Endpoint: /api/students/{id}/\
Method: DELETE\
Description: Delete a student \
Request:
```sh
curl -X DELETE http://127.0.0.1:8000/students/12/


```
#### Update a student
Endpoint: /api/students/{id}/\
Method: PUT\
Description: Modify Details of a Student\
Request:
```sh
curl -X PUT http://127.0.0.1:8000/api/students/9/ -H "Content-Type: application/json" -d '{
    "first_name": "Ammar",
    "last_name": "Younas",
    "email": "annar1@gmail.com",
    "date_of_birth": "2000-06-08"
}'
```
Response:
```sh
{"id":9,"first_name":"Ammar","last_name":"Younas","email":"annar1@gmail.com","date_of_birth":"2000-06-08"}
```
### Courses
#### List All Courses
Endpoint: /api/courses/\
Method: GET\
Description: Retrieves a list of all courses\
Request:
```sh
curl -X GET http://127.0.0.1:8000/api/courses/
```
Response:
```sh
[
{"id":2,"title":"SE","description":"Software Engineering","start_date":"2024-07-19","end_date":"2024-07-30"}
]
```
#### Get Single Course by ID
Endpoint: /api/courses/{id}/\
Method: GET\
Description: Retrieves a single course by id\
Request:
```sh
curl -X GET http://127.0.0.1:8000/api/students/2/
```
Response:
```sh
{"id":2,"title":"SE","description":"Software Engineering","start_date":"2024-07-19","end_date":"2024-07-30"}
```
#### Create a new course
Endpoint: /api/courses/\
Method: POST\
Description: Create a new course\
Request:
```sh
curl -X POST http://127.0.0.1:8000/api/courses/ -H "Content-Type: application/json" -d '{
    "title": "Organizational Behaviour",
    "description": "HRM-441",
    "start_date": "2023-09-01",
    "end_date": "2023-12-15"
}'

```
Response:
```sh
{"id":3,"title": "Organizational Behaviour", "description": "HRM-441","start_date": "2023-09-01","end_date": "2023-12-15"}'
```
#### Delete a course
Endpoint: /api/courses/{id}/\
Method: DELETE\
Description: Delete a course\
Request:
```sh
curl -X DELETE http://127.0.0.1:8000/courses/3/
```
#### Update a course
Endpoint: /api/courses/{id}/\
Method: PUT\
Description: Modify Details of a course\
Request:
```sh
curl -X POST http://127.0.0.1:8000/api/courses/3/ -H "Content-Type: application/json" -d '{
    "title": "OOP",
    "description": "CS-212",
    "start_date": "2024-09-01",
    "end_date": "2024-12-15"
}'
```
Response:
```sh
{"id":3,"title": "OOP", "description": "CS-212","start_date": "2024-09-01","end_date": "2024-12-15"}'
```
### Enrollments
#### List All Enrollments
Endpoint: /api/enrollments/\
Method: GET\
Description: Retrieves a list of all enrollments\
Request:
```sh
curl -X GET http://127.0.0.1:8000/api/enrollments/
```
Response:
```sh
[
{"id":1,"enrollment_date":"2024-07-21","student":6,"course":2},
{"id":2,"enrollment_date":"2024-07-21","student":10,"course":2},
{"id":3,"enrollment_date":"2024-07-21","student":15,"course":2}
]
```
#### Create a new Enrollment
Endpoint: /api/enrollments/\
Method: POST\
Description: Create a new enrollment\
Request:
```sh
curl -X POST http://127.0.0.1:8000/api/enrollments/ -H "Content-Type: application/json" -d '{
    "student": 10,
    "course": 2
}
```
Response:
```sh
{"id":6, "enrollment_date" : "2024-07-21", "student": 10, "course": 2}'
```

