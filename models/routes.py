from flask import request, jsonify
from app import app, db
from models import Restaurant, RestaurantPizza, Pizza

# Define the route to retrieve a list of pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        # Query all pizzas from the database and serialize them
        pizzas = Pizza.query.all()
        pizza_data = [pizza.serialize() for pizza in pizzas]
        return jsonify(pizza_data), 200
    except Exception as e:
        # Handle any errors and return an error response
        return jsonify({"error": str(e)}), 500

# Define the route to create a new RestaurantPizza entry
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate the data (check price, pizza_id, and restaurant_id)
        price = data.get("price")
        pizza_id = data.get("pizza_id")
        restaurant_id = data.get("restaurant_id")

        if not price or not isinstance(price, (int, float)) or not 1 <= price <= 30:
            return jsonify({"errors": ["Invalid price"]}), 400

        # Find the pizza and restaurant by IDs
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if pizza is None or restaurant is None:
            return jsonify({"errors": ["Invalid pizza or restaurant ID."]}), 400

        # Create a new RestaurantPizza entry
        restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)  # noqa: E501
        db.session.add(restaurant_pizza)
        db.session.commit()

        # Return data related to the pizza
        return jsonify(pizza.serialize()), 201  
    except Exception as e:
        # Handle any errors and return an error response
        return jsonify({"errors": [str(e)]}), 500