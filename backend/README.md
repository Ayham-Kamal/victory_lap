# Fitness Management Backend

## Overview
This is the backend for the fitness management web application, built using Flask, PostgreSQL, and Psycopg.
It provides APIs for user authentication, workout tracking, etc.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Navigate to the backend directory:
   ```bash
   cd backend
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python3 main.py
   ```

## API Endpoints

1. Signup:
   POST /auth/signup

   Request:
   ```json
   {
     "username": "test_user",
     "password": "securepassword"
   }
   ```
   Response:
   ```json
   {
     "message": "User created successfully."
   }
   ```
2. Login:
   POST /auth/login

   Request:
   ```json
   {
     "username": "test_user",
     "password": "securepassword"
   }
   ```

   Response:
   ```json
   {
     "message": "Login successful."
   }
   ```

3. User:
   GET /user/<user_id>

   Rsponse:
   ```json
   {
     "username": "test_user",
     "email": "test_user@mail.com",
     "weight(pounds)": 300
   }
   ```

4. Workout:
   POST /workout/log

   Request:
   ```json
   {
     "user_id": 1,
     "exercise": "Bench Press",
     "sets": 3,
     "reps": 10
   }
   ```

## Database
Ensure there is a '.env' file in the project's root directory.
Within this file add the url/DB connection. This will ensure our DB is not public facing.

1. Example:
   ```txt
    DATABASE_URL= '...'
   ```
