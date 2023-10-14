from sqlalchemy.sql import func
from main import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())  # NOW() ...
    bio = db.Column(db.Text)

    def __str__(self):
        return f"<Student {self.firstname}>"

    def __repr__(self):
        return f"<Student {self.firstname}>"


class Student1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())  # NOW() ...
    bio = db.Column(db.Text)

    def __str__(self):
        return f"<Student {self.firstname}>"

    def __repr__(self):
        return f"<Student {self.firstname}>"
