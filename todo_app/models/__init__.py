"""
This module initializes the models package for the Flask web application.

It imports the necessary models used throughout the application, making them available for use.

Modules:
    - User: Defines the User model for user authentication and management.
    - _ToDo: Defines the _ToDo model for managing user tasks.

Usage:
    This module should be imported whenever model access is required in the application.
"""

from .user import User  # Import the User model for user-related operations.
from .todo_models import ToDo  # Import the _ToDo model for task management.
