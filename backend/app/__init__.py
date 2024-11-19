from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Enable CORS for frontend-backend communication
    CORS(app)

    # Add a default route
    @app.route('/')
    def home():
        return 'Welcome to the API!'

    # Register blueprints (modularized routes)
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    from app.routes.workout import workout_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(workout_bp, url_prefix='/workout')

    return app
