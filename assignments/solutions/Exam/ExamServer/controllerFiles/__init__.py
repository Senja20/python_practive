from flask_restful import Api, reqparse
from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(__name__)

# initializing api that inherits from app
api = Api(app)

# initializing Marshmallow that inherits from app
ma = Marshmallow(app)


# creating Marshmallow schemas
class CarSchema(ma.Schema):
    class Meta:
        fields = ('license', 'model', 'price', 'producer', 'customer_number')


car_schema = CarSchema()
cars_schema = CarSchema(many=True)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('customerNumber', 'email', 'name', 'lastname')


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# initializing reqparse and setting it up for both car and customer
car_args = reqparse.RequestParser()  # reqparse for car
car_args.add_argument("license", type=str, help="License of the car is required", required=True)
car_args.add_argument("model", type=str, help="model of the car needs to be send")
car_args.add_argument("price", type=int, help="price of the car needs to be send")
car_args.add_argument("producer", type=str, help="The manufacturer of the car")

customer_args = reqparse.RequestParser()  # reqparse for customer
customer_args.add_argument("customerNumber", type=str, help="number of the customer is required", required=True)
customer_args.add_argument("name", type=str, help="first name of the customer")
customer_args.add_argument("email", type=str, help="email of the customer")
customer_args.add_argument("lastname", type=str, help="last name of the customer")
