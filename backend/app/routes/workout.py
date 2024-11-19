from flask import Blueprint, g, request, jsonify
from app.utils.db import execute_query
from backend.app.utils.jwt_helper import token_required

workout_bp = Blueprint('workout', __name__)

# Log a new workout
@workout_bp.route('/log', methods=['POST'])
@token_required
def log_workout():
    user_id = g.user_id  # Use JWT-authenticated user_id
    data = request.json
    workout_name = data.get('workout_name')
    muscle_group = data.get('muscle_group')
    duration = data.get('duration')  # ex: minutes

    # Validate inputs
    if not workout_name or not muscle_group or not duration:
        return jsonify({'error': 'All fields are required'}), 400

    # Insert workout into the database
    execute_query(
        "INSERT INTO workouts (user_id, workout_name, duration, calories_burned) VALUES (%s, %s, %s, %s)",
        (user_id, workout_name, muscle_group, duration)
    )
    return jsonify({'message': 'Workout logged successfully'}), 201

# View logged workouts
@workout_bp.route('/log', methods=['GET'])
@token_required
def view_workouts():
    user_id = g.user_id  # Use JWT-authenticated user_id

    # Retrieve workouts from the database
    results = execute_query(
        "SELECT id, workout_name, duration, calories_burned FROM workouts WHERE user_id = %s",
        (user_id,), fetchall=True
    )
    if results:
        return jsonify(results), 200
    return jsonify({'error': 'No workouts found'}), 404

# Delete a logged workout
@workout_bp.route('/log', methods=['DELETE'])
def delete_workout():
    data = request.json
    workout_id = data.get('workout_id')

    # Delete the workout from the database
    execute_query("DELETE FROM workouts WHERE id = %s", (workout_id,))
    return jsonify({'message': 'Workout deleted successfully'}), 200
