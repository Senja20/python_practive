from ExamServer.modelFiles import app
from ExamServer.controllerFiles import api
from ExamServer.controllerFiles.services import CarHandel, CustomerHandler, rentHandler

# controllerFiles contains api

# 25% Integrate the frontend with the backend REST API
api.add_resource(CarHandel, '/car')     # 10% Implement the API that handles cars
api.add_resource(CustomerHandler, '/customer')  # 10% Implement the API that handles customers
api.add_resource(rentHandler, '/rent')  # 10% Implement the API that handles car to customer assignment

if __name__ == '__main__':
    app.run(debug=True)
