User Management Module for Ecommerce Project
Welcome to the User Management Module of the Ecommerce Project. This module provides essential user management functionalities such as registration, login, profile management, and password reset. It is built using Django and Django REST Framework.

Overview
This module includes the following features:

User Registration
User Login
Profile Retrieval and Update
Password Reset
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.x
pip (Python package installer)
Django
Django REST Framework
Django REST Framework Authtoken
Installation
Clone the Repository


git clone https://github.com/Shahbajkhan2023/user_management_api.git
cd ecommerce_project
Create and Activate a Virtual Environment


python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies

pip install -r requirements.txt
Apply Migrations


python manage.py migrate
Create a Superuser


python manage.py createsuperuser
Run the Development Server


python manage.py runserver
API Endpoints
1. Register a New User
URL: /api/users/register/
Method: POST
Description: Registers a new user.
Request Body:
{
  "email": "user@example.com",
  "password": "yourpassword",
  "password2": "yourpassword"
}

Response:
{
  "email": "user@example.com",
  "token": "your_auth_token"
}

2. Login User
URL: /api/users/login/
Method: POST
Description: Authenticates a user and returns an authentication token.
Request Body:
{
  "email": "user@example.com",
  "password": "yourpassword"
}
Response:
{
  "token": "your_auth_token"
}

3. Retrieve or Update User Profile
URL: /api/users/profile/
Method: GET / PUT
Description: Retrieves or updates the logged-in user’s profile. Requires authentication.
Request Headers:
makefile
Authorization: Token your_auth_token
GET Response:
{
  "email": "user@example.com"
}
PUT Request Body:
{
  "email": "new_email@example.com"
}
PUT Response:
{
  "email": "new_email@example.com"
}

4. Password Reset
URL: /api/users/password-reset/
Method: POST
Description: Sends a password reset email to the specified email address.
Request Body:
{
  "email": "user@example.com"
}
Response:
{
  "message": "Password reset email sent"
}
