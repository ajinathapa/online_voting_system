import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # or PostgreSQL/MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False