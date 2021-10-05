from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class adopt(db.Model):
    """Adopt Model"""

    __tablename__ = "adopt"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default="/static/default_photo.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    availability = db.Column(db.Boolean, default=True)
