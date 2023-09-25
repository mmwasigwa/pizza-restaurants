from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Pizza import Pizza
from models.Restaurant import Restaurant
from models.RestaurantPizza import RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzadatabase.db'
db = SQLAlchemy(app)

# Define your models (Restaurant, Pizza, RestaurantPizza) here

# Define the GET /pizzas route to return a list of pizzas in JSON format
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        # Query all pizzas from the database and serialize them
        pizzas = Pizza.query.all()
        pizza_data = [pizza.serialize() for pizza in pizzas]
        return jsonify(pizza_data)
    except Exception as e:
        # Handle any errors and return an error response
        return jsonify({"error": str(e)}), 500

# Define the POST /restaurant_pizzas route to create a new RestaurantPizza entry
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
            return jsonify({"errors": ["Invalid price. Price must be between 1 and 30."]}), 400

        # Find the pizza and restaurant by IDs
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if pizza is None or restaurant is None:
            return jsonify({"errors": ["Invalid pizza or restaurant ID."]}), 400

        # Create a new RestaurantPizza entry
        restaurant_pizza = RestaurantPizza(price=price, pizza=pizza,
                                            restaurant=restaurant)
        db.session.add(restaurant_pizza)
        db.session.commit()

        # Return data related to the pizza
        return jsonify(pizza.serialize()), 201
    except Exception as e:
        # Handle any errors and return an error response
        return jsonify({"errors": [str(e)]}), 500

if __name__ == '__main__':
    app.run(debug=True)