from flask import request, jsonify
from app import app, db
from models import Restaurant, RestaurantPizza, Pizza

# Define the route to retrieve a list of pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_data = [pizza.serialize() for pizza in pizzas]
    return jsonify(pizza_data)

# Define the route to create a new RestaurantPizza entry
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price, pizza_id, restaurant_id = data.get("price"), data.get("pizza_id"), data.get("restaurant_id")  # noqa: E501

    if not price or not isinstance(price, (int, float)) or not 1 <= price <= 30:
        return jsonify({"errors": ["Invalid price"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid pizza or restaurant ID."]}), 400

    restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify(pizza.serialize()), 201
