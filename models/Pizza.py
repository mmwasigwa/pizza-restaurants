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
