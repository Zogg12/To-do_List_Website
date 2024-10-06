"""
This module initializes the Flask web application, sets up the database, and configures user authentication.

Attributes:
    db (SQLAlchemy): The SQLAlchemy database instance used for database operations.
    login_manager (LoginManager): The Flask-Login manager instance for user session management.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

# Initialize extensions that will be used with the app
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask application with configurations from
    the Config class, sets up database connectivity, and configures user
    authentication through Flask-Login. It also registers the main blueprint
    for routing.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    from .models import User  # Ensure you import the User model

    @login_manager.user_loader
    def load_user(user_id):
        """
        Load a user from the database by user ID.

        This function is used by Flask-Login to retrieve a user object from
        the database using the provided user ID.

        Args:
            user_id (int): The ID of the user to be loaded.

        Returns:
            User: The user object if found, None otherwise.
        """
        return User.query.get(int(user_id))

    db.init_app(app)  # Initialize the database with the app
    login_manager.init_app(app)  # Initialize Flask-Login with the app
    login_manager.login_view = 'main.login'  # Redirect to /login view
    login_manager.login_message = 'Please log in to access this page.'  # Message to show when login is required

    # Import the routes blueprint here to avoid circular import issues
    from .routes import main  # Import the main blueprint (collection of routes) to the app
    app.register_blueprint(main)  # Register the blueprint with the app

    return app  # Return the configured Flask application
