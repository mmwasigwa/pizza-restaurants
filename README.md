# Flask Code Challenge - Pizza Restaurants

## Table of Contents :

- [Introduction](#introduction)
- [Technologies Used](#technologies_used)
- [Project Structure](#project_structure)
- [Models](#models)
  - [Restaurant](#restaurant)
  - [Pizza](#pizza)
  - [RestaurantPizza](#restaurantpizza)
- [Validations](#validations)
- [Routes](#routes)
  - [GET /restaurants](#get-restaurants)
  - [GET /restaurants/:id](#get-restaurantsid)
  - [DELETE /restaurants/:id](#delete-restaurantsid)
  - [GET /pizzas](#get-pizzas)
  - [POST /restaurant_pizzas](#post-restaurant_pizzas)
- [Acknowledgement](#acknowledgement)
- [Author's Info](#authors_info)
- [Contact Author](#contact)
  

## Introduction

In this *Flask Code Challenge*, you will build a Flask API for managing Pizza Restaurants, Pizzas, and their associations. This API will provide endpoints to perform various operations related to these entities.

## Models

You need to create the following models:

### Restaurant

- Attributes:
  - `id` (Integer, Primary Key)
  - `name` (String, Unique, Not Null, Max Length: 50)
  - `address` (String, Not Null, Max Length: 255)

- Relationships:
  - A Restaurant has many Pizzas through RestaurantPizza.

### Pizza

- Attributes:
  - `id` (Integer, Primary Key)
  - `name` (String, Not Null, Max Length: 50)
  - `ingredients` (String, Not Null, Max Length: 255)

- Relationships:
  - A Pizza has many Restaurants through RestaurantPizza.

### RestaurantPizza

- Attributes:
  - `id` (Integer, Primary Key)
  - `price` (Float, Not Null)

- Relationships:
  - A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.

## Validations

- Add the following validations to the models:

### RestaurantPizza Model

- `price` must have a value between 1 and 30.

### Restaurant Model

- `name` must have a length less than 50 characters.
- `name` must be unique.

## Routes

Set up the following routes for your API:

***GET /restaurants**

- Returns JSON data in the format:
  ```json
  [
    {
      "id": 1,
      "name": "Dominion Pizza",
      "address": "Good Italian, Ngong Road, 5th Avenue"
    },
    {
      "id": 2,
      "name": "Pizza Hut",
      "address": "Westgate Mall, Mwanzi Road, Nrb 100"
    }
  ]
  ```
  If the Restaurant does not exist, returns JSON data with the appropriate HTTP status code:

```
{
  "error": "Restaurant not found"
}
```
**DELETE /restaurants/:id**

If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it.

After deleting the Restaurant, returns an empty response body with the appropriate HTTP status code.

If the Restaurant does not exist, returns JSON data with the appropriate HTTP status code:
```
{
  "error": "Restaurant not found"
}
GET /pizzas
```
Returns JSON data in the format:
```
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```
**POST /restaurant_pizzas**

This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant.

It should accept an object with the following properties in the body of the request:
```
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:
```
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```
If the RestaurantPizza is not created successfully, return the following JSON data, along with the appropriate HTTP status code:
```
{
  "errors": ["validation
  ```