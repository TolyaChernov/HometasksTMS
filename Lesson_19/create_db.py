from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import Users, app, db

with app.app_context():
    db.create_all()
