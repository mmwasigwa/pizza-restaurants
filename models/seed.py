from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    try:
        # Create restaurants
        restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
        restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")
        restaurant3 = Restaurant(name="CJs", address="Koinange St")
        restaurant4 = Restaurant(name="Java House", address="Prestige Mall, Ngong Rd")
        restaurant5 = Restaurant(name="Mama's", address="Ngong Rd")
        restaurant6 = Restaurant(name="DoubleTree by Hilton", address="Ngong Lane, Ngong Rd")
        restaurant7 = Restaurant(name="Nyama Choma Spot", address="Mombasa Rd")
        restaurant8 = Restaurant(name="Tom's Diner", address="James Gichuru Rd")

        # Create pizza
        pizza1 = Pizza(name="Margherita Pizza", ingredients="Tomato sauce, mozzarella cheese, fresh basil leaves, olive oil, salt")
        pizza2 = Pizza(name="Pepperoni Pizza", ingredients="Pepperoni, Cheese, mozzarella cheese, pepperoni slices")
        pizza3 = Pizza(name="Hawaiian Pizza", ingredients="Tomato sauce, mozzarella cheese, ham or Canadian bacon, pineapple")
        pizza4 = Pizza(name="Supreme Pizza", ingredients="Tomato sauce, mozzarella cheese, pepperoni, sausage, bell peppers")
        pizza5 = Pizza(name="BBQ Chicken Pizza", ingredients="Barbecue sauce (instead of tomato sauce), mozzarella cheese, grilled chicken")

        # Add objects to the session and commit
        db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5, restaurant6, restaurant7, restaurant8])
        db.session.add_all([pizza1, pizza2, pizza3, pizza4, pizza5])
        db.session.commit()

        # Create restaurant pizzas
        restaurant_pizza1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=22)
        restaurant_pizza2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=30)
        restaurant_pizza3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza2, price=25)

        db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
        db.session.commit()

        print("Database seeding completed successfully.")
    except Exception as e:
        # Handle any errors and roll back the transaction
        db.session.rollback()
        print(f"Error: {str(e)}")