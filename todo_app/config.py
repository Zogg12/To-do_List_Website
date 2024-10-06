"""
Configuration settings for the Flask application.

Attributes:
    SECRET_KEY (str): Secret key for session management.
    SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable modification tracking for performance.
"""


from os import environ

class Config:
    """Base configuration."""
    SECRET_KEY = environ.get('SECRET_KEY') or 'SuperSecretKey'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///to-do-sqlite3.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
