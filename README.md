BACKEND Task Manager API - Django REST Framework

Overview

A simple Task Manager API built with Django REST Framework that allows you to create, read, update, and delete tasks with features like due dates, completion status, and sorting.

Features

CRUD Operations: Create, Read, Update, and Delete tasks

Task Attributes:

Name

Description

Completion status

Due date

Completion date

Sorting & Filtering: Sort by due date, creation date, or completion status

Pagination: Results are paginated for better performance

API Endpoints
Base URL

http://localhost:8000/api/

Available Endpoints

Endpoint	Method	Description	Example

/tasks/	GET	List all tasks (with optional sorting)	GET /api/tasks/?ordering=-due_date

/tasks/	POST	Create a new task	POST /api/tasks/

/tasks/<id>/	GET	Retrieve a specific task	GET /api/tasks/1/

/tasks/<id>/	PUT	Fully update a task	PUT /api/tasks/1/

/tasks/<id>/	PATCH	Partially update a task	PATCH /api/tasks/1/

/tasks/<id>/	DELETE	Delete a task	DELETE /api/tasks/1/
