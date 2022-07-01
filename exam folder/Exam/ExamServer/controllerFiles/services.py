from flask import jsonify
from flask_restful import Resource, abort

from ExamServer.modelFiles.model import db
from ExamServer.modelFiles.model import Customers, Cars
from ExamServer.controllerFiles import car_schema, cars_schema, customer_schema, customers_schema, customer_args, car_args


# services contains Resources that are used by api

# Resources that are being used by api
class CarHandel(Resource):
    def get(self):
        result = Cars.query.all()
        return cars_schema.jsonify(result)

    def post(self):
        args = car_args.parse_args()
        requested_car = Cars.query.filter_by(license=args["license"]).first()
        if requested_car:
            abort(409, message="Car license already exists")

        else:
            car_new = Cars(license=args["license"], model=args["model"], price=args["price"], producer=args["producer"])
            db.session.add(car_new)
            db.session.commit()

            return car_schema.jsonify(car_new)

    def put(self):
        args = car_args.parse_args()
        request = Cars.query.filter_by(license=args["license"]).first()

        if not request:
            abort(404, message="The car does not exist")
        else:
            request.model = args["model"]
            request.price = args['price']
            request.producer = args["producer"]
            db.session.commit()
            return car_schema.jsonify(request)

    def delete(self):
        args = car_args.parse_args()
        request_delete = Cars.query.filter_by(license=args["license"]).first()

        if request_delete:
            db.session.delete(request_delete)
            db.session.commit()
            return jsonify({"message": "The car was successfully removed"})

        else:
            abort(404, message="The car does not exist")


class CustomerHandler(Resource):
    def get(self):
        customers = Customers.query.all()
        return customers_schema.jsonify(customers)

    def post(self):
        args = customer_args.parse_args()
        requested_customer = Customers.query.filter_by(customerNumber=args["customerNumber"]).first()
        if requested_customer:
            abort(409, message="this customer number already exists")
        else:
            customer_new = Customers(customerNumber=args["customerNumber"], name=args["name"],
                                     lastname=args["lastname"], email=args["email"])
            db.session.add(customer_new)
            db.session.commit()
            return customer_schema.jsonify(customer_new)

    def put(self):
        args = customer_args.parse_args()
        customer = Customers.query.filter_by(customerNumber=args["customerNumber"]).first()

        if not customer:
            abort(404, message="The customer does not exist")
        else:
            customer.email = args["email"]
            customer.name = args['name']
            customer.lastname = args["lastname"]
            db.session.commit()
            return customer_schema.jsonify(customer)

    def delete(self):
        args = customer_args.parse_args()
        request_delete = Customers.query.filter_by(customerNumber=args["customerNumber"]).first()

        if request_delete:
            db.session.delete(request_delete)
            db.session.commit()
            return jsonify({"message": "The customer was successfully removed"})
        else:
            abort(404, message="The customer does not exist")


class rentHandler(Resource):
    def post(self):
        args_car = car_args.parse_args()
        args_customer = customer_args.parse_args()

        request_car = Cars.query.filter_by(license=args_car["license"]).first()
        request_customer = Customers.query.filter_by(customerNumber=args_customer["customerNumber"]).first()

        if not request_customer:
            abort(404, messege="Customer does not exist")
        elif request_car.customer_number is not None:
            abort(400, messege="This car is already rented")
        else:
            request_car.customer_number = args_customer["customerNumber"]
            db.session.commit()
            requestCar = Cars.query.filter_by(license=args_car["license"]).first()
            return car_schema.jsonify(requestCar)

    def put(self):
        args_car = car_args.parse_args()

        request_car = Cars.query.filter_by(license=args_car["license"]).first()

        if request_car:
            temp_license = request_car.license
            temp_model = request_car.model
            temp_price = request_car.price
            temp_manufacturer = request_car.producer

            db.session.delete(request_car)
            db.session.commit()

            new_replaced = Cars(license=temp_license, model=temp_model, price=temp_price, producer=temp_manufacturer)
            db.session.add(new_replaced)
            db.session.commit()

            return car_schema.jsonify(new_replaced)
        else:
            return abort(404, messege="Car does not exist")
