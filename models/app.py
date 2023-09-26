from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, reqparse
from models import db, Pizza, Restaurant, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzadatabase.db'
migrate_app = Migrate(app,db)
db.init_app(app)
ma = Marshmallow(app)
api = Api(app)

#schemas

# Pizzas Schema
class PizzaSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Pizza

    # id = ma.auto_field()

Pizza_schema = PizzaSchema()
Pizzas_schema = PizzaSchema(many=True)

# Restaurant Schema


class RestaurantSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Restaurant

   # Restaurant = ma.auto_field()

Restaurant_schema = RestaurantSchema()
Restaurants_schema = RestaurantSchema(many=True)

# Restaurant_Pizzas Schema

class Restaurant_PizzaSchema(ma.SQLAlchemySchema):

    class Meta:
        model = RestaurantPizza

    # RestaurantPizza = ma.auto_field()

Restaurant_Pizza_schema = Restaurant_PizzaSchema()
Restaurant_Pizzas_schema = Restaurant_PizzaSchema(many=True)



# Define the route to create a new RestaurantPizza entry
class RestaurantPizzaResource(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("price", type=float, required=True)
            parser.add_argument("pizza_id", type=int, required=True)
            parser.add_argument("restaurant_id", type=int, required=True)
            args = parser.parse_args()

            price = args["price"]
            pizza_id = args["pizza_id"]
            restaurant_id = args["restaurant_id"]

            if not 1 <= price <= 30:
                return {"errors": ["Invalid price"]}, 400

            pizza = Pizza.query.get(pizza_id)
            restaurant = Restaurant.query.get(restaurant_id)

            if pizza is None or restaurant is None:
                return {"errors": ["Invalid pizza or restaurant ID."]}, 400

            restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
            db.session.add(restaurant_pizza)
            db.session.commit()

            return Pizza_schema.dump(pizza), 201
        except Exception as e:
            return {"errors": [str(e)]}, 500

api.add_resource(RestaurantPizzaResource, "/restaurant_pizzas")

# Define the GET /pizzas route to return a list of pizzas in JSON format
class PizzaListResource(Resource):
    def get(self):
        try:
            pizzas = Pizza.query.all()
            return Pizza_schema.dump(pizzas, many=True)
        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(PizzaListResource, "/pizzas")

# Define the GET /restaurants route to return a list of restaurants in JSON format
class RestaurantListResource(Resource):
    def get(self):
        try:
            restaurants = Restaurant.query.all()
            return Restaurant_schema.dump(restaurants, many=True)
        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(RestaurantListResource, "/restaurants")

# Define the GET /restaurants/:id route to return a specific restaurant by ID
class RestaurantResource(Resource):
    def get(self, id):
        try:
            restaurant = Restaurant.query.get(id)
            if restaurant:
                return Restaurant_schema.dump(restaurant)
            return {"error": "Restaurant not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(RestaurantResource, "/restaurants/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)