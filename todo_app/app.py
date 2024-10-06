"""
This module serves as the entry point for the Flask web application.

It initializes the Flask application, sets up the database, and starts the development server.

Attributes:
    app: An instance of the Flask application created using the `create_app()` function.

Usage:
    To run the application, execute this module directly. The database will be set up before the server starts.
"""

from todo_app import create_app, db

app = create_app()  # Create an instance of the Flask application using the create_app function.

if __name__ == "__main__":  # Check if this script is being run as the main program.
    # If this script is executed directly (not imported), __name__ will be '__main__'.

    with app.app_context():  # Create an application context to work with the app and its resources.
        db.create_all()

    app.run(debug=False)
