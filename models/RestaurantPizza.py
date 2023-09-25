from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
             # Include pizza details in serialization
            "restaurant": self.restaurant.serialize()  
        }
            # Include restaurant details in serialization