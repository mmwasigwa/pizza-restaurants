from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    # Define the relationship with RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)  # noqa: E501

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
