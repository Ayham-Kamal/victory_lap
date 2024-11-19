from flask import Blueprint, request, jsonify
from app.utils.bcrypt_helper import hash_password, check_password
from app.utils.db import execute_query
import jwt
import os
from datetime import datetime, timedelta


SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # Store this in .env
if not SECRET_KEY:
    raise ValueError("JWT_SECRET_KEY is not set in the environment.")

def generate_jwt(user_id):
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
    payload = {
        "user_id": user_id,
        "exp": expiration,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Hash password and store it in the database
    hashed_pw = hash_password(password)
    execute_query("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
    return jsonify({'message': 'Signup successful'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Retrieve user data from database
    result = execute_query("SELECT password FROM users WHERE username = %s", (username,), fetchone=True)
    if result and check_password(password, result[1]):  # result[1] is the hashed password
        token = generate_jwt(result[0])  # result[0] is the user_id
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
