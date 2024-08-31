# StudySphere Backend

Welcome to the StudySphere Backend repository! This project provides the server-side infrastructure for the StudySphere platform, handling data management, user authentication, and other essential backend functionalities.

## 🎯 Project Description

The StudySphere Backend is built using Django and Django Rest Framework (DRF), designed to deliver a robust and scalable API service. It supports various operations related to user management, tuition applications, and more.

## 🌟 Key Features

- **RESTful API Endpoints**: Exposes various endpoints for interacting with the platform.
- **User Authentication**: Handles user registration, login, and profile management.
- **Data Management**: Manages data related to tuitions, applications, and reviews.
- **Error Handling**: Provides appropriate error messages and status codes.
- **Secure**: Implements security best practices for user data and transactions.

## 🛠 Technologies & Tools

- **Django**: High-level Python web framework for rapid development.
- **Django Rest Framework (DRF)**: Powerful and flexible toolkit for building Web APIs.
- **Python**: Programming language used for backend development.
- **PostgreSQL**: Database management system for storing data.
- **Django Allauth**: Authentication system for handling user registration and login.
- **Django Cors Headers**: Handles Cross-Origin Resource Sharing (CORS) to allow requests from different domains.

## 🏗 API Endpoints

### User Management

- **Register User**
  - `POST /accounts/new_user/register/`
  - **Description**: Registers a new user.
  - **Body**: `{ "username": "string", "email": "string", "password": "string" }`

- **Login User**
  - `POST /accounts/user/login/`
  - **Description**: Authenticates a user and returns a token.
  - **Body**: `{ "username": "string", "password": "string" }`

- **Get User Profile**
  - `GET /accounts/id`
  - **Description**: Retrieves the profile information of the authenticated user.
  - **Headers**: `Authorization: Token ${token}`

- **Change Password**
  - `POST /accounts/user/change_password/`
  - **Description**: Allows users to change their password.
  - **Body**: `{ "old_password": "string", "new_password": "string", "confirm_password": "string" }`
  - **Headers**: `Authorization: Bearer <token>`

### Tuition Management

- **Get Tuition List**
  - `GET /tuitions/list`
  - **Description**: Retrieves a list of available tuitions.

- **Create Tuition**
  - `POST /api/tuitions/`
  - **Description**: Creates a new tuition entry.
  - **Body**: `{ "title": "string", "description": "string", "price": "number" }`
  - **Headers**: `Authorization: Bearer <token>`

- **Update Tuition**
  - `PUT /api/tuitions/{id}/`
  - **Description**: Updates a tuition entry.
  - **Body**: `{ "title": "string", "description": "string", "price": "number" }`
  - **Headers**: `Authorization: Bearer <token>`

- **Delete Tuition**
  - `DELETE /api/tuitions/{id}/`
  - **Description**: Deletes a tuition entry.
  - **Headers**: `Authorization: Bearer <token>`

### Application Management

- **Apply for Tuition**
  - `POST /api/application/`
  - **Description**: Applies for a tuition.
  - **Body**: `{ "tuition_id": "integer", "user_id": "integer" }`
  - **Headers**: `Authorization: Bearer <token>`

- **Get User Applications**
  - `GET /api/application/`
  - **Description**: Retrieves applications made by the authenticated user.
  - **Headers**: `Authorization: Bearer <token>`

### Review Management

- **Submit Review**
  - `POST /api/review/`
  - **Description**: Submits a review for a tuition.
  - **Body**: `{ "tuition_id": "integer", "rating": "integer", "comment": "string" }`
  - **Headers**: `Authorization: Bearer <token>`

- **Get Reviews for Tuition**
  - `GET /api/review/{tuition_id}/`
  - **Description**: Retrieves reviews for a specific tuition.

## 🛠 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/arasruislam/StudySphere-Backend.git
