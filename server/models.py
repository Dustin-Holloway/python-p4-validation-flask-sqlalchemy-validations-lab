from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("failed")
        return name

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if not len(phone_number) == 10:
            raise ValueError("The number is not 10 digits long")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError("Content too short")

    @validates("summary")
    def validate_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError

    @validates("title")
    def validate_title(self, key, value):
        if not value:
            raise ValueError
        elif value != "":
            raise ValueError
        elif value not in ["Won't Believe", "Secret", "Top", "Guess"]:
            raise ValueError

    @validates("category")
    def validate_category(self, key, cat):
        if cat not in ["Non-Fiction", "Fiction"]:
            raise ValueError("Invalid category")

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"
