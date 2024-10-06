"""
This module defines the main blueprint for the application.

Attributes:
    main (Blueprint): The main blueprint instance for organizing routes.

The main blueprint serves as a central location for routing and
organizing the application's views and functionalities. It imports
the authentication routes and to-do routes to provide a cohesive
structure for the application.
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from .auth import *  # Import authentication routes
from .todo_routes import *  # Import to-do related routes
