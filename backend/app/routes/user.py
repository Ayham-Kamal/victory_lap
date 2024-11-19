from flask import Blueprint, request, jsonify
from app.utils.db import execute_query

user_bp = Blueprint('user', __name__)

# Get User Profile
@user_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')  # Fetch user ID from query params

    # Query database for user information
    result = execute_query("SELECT username, email FROM users WHERE id = %s", (user_id,), fetchone=True)

    if result:
        return jsonify({'username': result[0], 'email': result[1]}), 200
    return jsonify({'error': 'User not found'}), 404

# Update User Profile
@user_bp.route('/profile', methods=['PUT'])
def update_profile():
    data = request.json
    user_id = data.get('user_id')
    new_username = data.get('username')
    new_email = data.get('email')

    # Update user information in the database
    execute_query(
        "UPDATE users SET username = %s, email = %s WHERE id = %s",
        (new_username, new_email, user_id)
    )
    return jsonify({'message': 'Profile updated successfully'}), 200

# Delete User Account
@user_bp.route('/profile', methods=['DELETE'])
def delete_profile():
    data = request.json
    user_id = data.get('user_id')

    # Delete the user from the database
    execute_query("DELETE FROM users WHERE id = %s", (user_id,))
    return jsonify({'message': 'Account deleted successfully'}), 200
