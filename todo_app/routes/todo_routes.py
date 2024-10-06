"""
This module contains the routes related to the to-do functionality of the application.

Routes:
    / (GET): Home route that shows all tasks for the logged-in user.
    /add (POST): Add a new to-do item.
    /update/<int:todo_id> (GET): Update the status of a to-do item.
    /delete/<int:todo_id> (GET): Delete a to-do item from the list.
"""

from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import ToDo


@main.route('/')
@login_required
def index():
    """Home route that shows all tasks for the logged-in user.

    Retrieves all to-do items associated with the current user and
    renders the index template with the list of tasks.

    Returns:
        Response: Renders the index.html template with the user's to-do items.
    """
    todos = ToDo.query.filter_by(owner=current_user).all()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
@login_required
def add_todo():
    """Add a new to-do item.

    Extracts the task from the form submission and creates a new
    _ToDo object associated with the current user, then commits it
    to the database.

    Returns:
        Response: Redirects to the main index route after adding the to-do item.
    """
    task = request.form.get('task')
    new_todo = ToDo(task=task, owner=current_user, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/update/<int:todo_id>')  # Define a dynamic route for updating a to-do item
@login_required
def update(todo_id):
    """Update the status of a to-do item as completed or not.

    Toggles the completion status of the specified to-do item
    and commits the change to the database.

    Args:
        todo_id (int): The ID of the to-do item to update.

    Returns:
        Response: Redirects to the main index route after updating the to-do item.
    """
    task = ToDo.query.get(todo_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/delete/<int:todo_id>')  # Define a dynamic route for deleting a to-do item
@login_required
def delete(todo_id):
    """Delete a to-do item from the list.

    Retrieves the specified to-do item and removes it from the
    database.

    Args:
        todo_id (int): The ID of the to-do item to delete.

    Returns:
        Response: Redirects to the main index route after deleting the to-do item.
    """
    task = ToDo.query.get(todo_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
