from app import db
from models import Restaurant

new_restaurant = Restaurant(name="Pizza Palace", address="123 Main St")

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __init__(self, name, address):
        self.name = name
        self.address = address