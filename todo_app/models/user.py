"""
This module defines the User model for the application.

The User model represents a user in the system, including their
username, password, and associated to-do items.
"""

from flask_login import UserMixin
from .. import db


class User(db.Model, UserMixin):
    """
    Represents a user in the application.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): The user's username, must be unique.
        password (str): The user's password.
        todos (list): A list of _ToDo items associated with the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    todos = db.relationship('ToDo', backref='owner', lazy=True)
