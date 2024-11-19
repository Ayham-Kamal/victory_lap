from flask import Blueprint, request, jsonify
from app.utils.bcrypt_helper import hash_password, check_password
from app.utils.db import execute_query

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

    # Retrieve hashed password from database
    result = execute_query("SELECT password FROM users WHERE username = %s", (username,), fetchone=True)
    if result and check_password(password, result[0]):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
