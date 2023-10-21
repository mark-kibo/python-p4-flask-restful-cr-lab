from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))

    image = db.Column(db.String(255))  # I increased the length to 255 for image URLs, adjust as needed
    price = db.Column(db.DECIMAL(10, 2))
