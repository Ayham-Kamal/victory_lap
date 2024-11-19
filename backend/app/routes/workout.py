from flask import Blueprint, request, jsonify
from app.utils.db import execute_query

workout_bp = Blueprint('workout', __name__)

# Log a new workout
@workout_bp.route('/log', methods=['POST'])
def log_workout():
    data = request.json
    user_id = data.get('user_id')
    workout_name = data.get('workout_name')
    muscle_group = data.get('muscle_group')
    duration = data.get('duration')  # ex: minutes

    # Insert workout into the database
    execute_query(
        "INSERT INTO workouts (user_id, workout_name, duration, calories_burned) VALUES (%s, %s, %s, %s)",
        (user_id, workout_name, muscle_group, duration)
    )
    return jsonify({'message': 'Workout logged successfully'}), 201

# View logged workouts
@workout_bp.route('/log', methods=['GET'])
def view_workouts():
    user_id = request.args.get('user_id')  # Fetch user ID from query params

    # Retrieve workouts from the database
    results = execute_query(
        "SELECT id, workout_name, duration, calories_burned FROM workouts WHERE user_id = %s",
        (user_id,), fetchall=True
    )
    return jsonify({'error': 'No workouts found'}), 404

# Delete a logged workout
@workout_bp.route('/log', methods=['DELETE'])
def delete_workout():
    data = request.json
    workout_id = data.get('workout_id')

    # Delete the workout from the database
    execute_query("DELETE FROM workouts WHERE id = %s", (workout_id,))
    return jsonify({'message': 'Workout deleted successfully'}), 200
