from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  
class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    # Define the relationship with RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    # Define foreign keys for the relationships with Restaurant and Pizza
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # noqa: E501
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza": self.pizza.serialize(),
            "restaurant": self.restaurant.serialize()
        }

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