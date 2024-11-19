from flask import Blueprint, g, request, jsonify
from app.utils.db import execute_query
from backend.app.utils.jwt_helper import token_required

user_bp = Blueprint('user', __name__)

# Get User Profile
@user_bp.route('/profile', methods=['GET'])
@token_required
def get_profile():
    user_id = g.user_id  # Extracted from the token by the decorator
    result = execute_query("SELECT username, email FROM users WHERE id = %s", (user_id,), fetchone=True)
    if result:
        return jsonify({'username': result[0], 'email': result[1]}), 200
    return jsonify({'error': 'User not found'}), 404

# Update User Profile
@user_bp.route('/profile', methods=['PUT'])
@token_required
def update_profile():
    user_id = g.user_id  # Use JWT-authenticated user_id
    data = request.json
    new_username = data.get('username')
    new_email = data.get('email')

    # Validate inputs (optional but recommended)
    if not new_username or not new_email:
        return jsonify({'error': 'Username and email are required'}), 400

    # Update user information in the database
    execute_query(
        "UPDATE users SET username = %s, email = %s WHERE id = %s",
        (new_username, new_email, user_id)
    )
    return jsonify({'message': 'Profile updated successfully'}), 200


# Delete User Account
@user_bp.route('/profile', methods=['DELETE'])
@token_required
def delete_profile():
    user_id = g.user_id  # Use JWT-authenticated user_id
    execute_query("DELETE FROM users WHERE id = %s", (user_id,))
    return jsonify({'message': 'Account deleted successfully'}), 200
