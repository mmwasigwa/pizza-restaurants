# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    # Define Restaurant model fields here
    pass

class Pizza(db.Model):
    # Define Pizza model fields here
    pass

class RestaurantPizza(db.Model):
    # Define RestaurantPizza model fields here
    pass
