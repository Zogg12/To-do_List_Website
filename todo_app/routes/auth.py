"""
This module contains the authentication routes for the application.

Routes:
    /login (GET, POST): Log in a user.
    /logout (GET): Log out the current user.
    /register (GET, POST): Register a new user.
"""

from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import main
from .. import db
from ..models import User


@main.route('/login', methods=['GET', 'POST'])
def login():
    """Log in a user.

    If the request method is POST, it verifies the user's credentials
    and logs in the user if they are valid. Otherwise, it renders
    the login page.

    Returns:
        Response: Redirects to the main index if login is successful,
                  or renders the login template.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Login failed. Check your username and password.")
            return redirect(url_for('main.login'))

        login_user(user)
        return redirect(url_for('main.index'))

    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    """Log out the current user.

    Logs out the user and redirects to the login page.

    Returns:
        Response: Redirects to the login route after logging out.
    """
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user.

    If the request method is POST, it processes the registration
    form, checks for existing users, and creates a new user
    if the username is available. Otherwise, it renders the
    registration page.

    Returns:
        Response: Redirects to the login route upon successful registration,
                  or renders the registration template.
    """
    if request.method == 'POST':
        fetched_username = request.form.get('username')
        fetched_password = request.form.get('password')
        hashed_password = generate_password_hash(fetched_password, method='pbkdf2:sha256')

        # Check if user already exists
        existing_user = User.query.filter_by(username=fetched_username).first()
        if existing_user:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for('main.register'))

        new_user = User(username=fetched_username, password=hashed_password)  # noqa (disable linter warning)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for('main.login'))

    return render_template('register.html')
