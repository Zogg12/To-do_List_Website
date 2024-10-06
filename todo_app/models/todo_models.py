"""
This module defines the _ToDo model for the application.

The _ToDo model represents a to-do item associated with a user,
including its task description and completion status.
"""

from .. import db

class ToDo(db.Model):
    """
    Represents a to-do item in the application.

    Attributes:
        id (int): Unique identifier for the to-do item.
        task (str): The task description.
        user_id (int): The ID of the user associated with this to-do item.
        completed (bool): Indicates whether the task is completed.
    """

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
