from tkinter import *
import requests

URL = "http://127.0.0.1:5000/car"


# car related functions
def Clicked_btn_send_car_add(self):
    car_license = self.enter_license.get()
    Model_name_car = self.enter_model.get()
    car_producer = self.enter_manufacturer.get()
    price_car = self.enter_price.get()

    new_car = {
        "license": f"{car_license}",
        "model": f"{Model_name_car}",
        "producer": f"{car_producer}",
        "price": price_car
    }

    # sending a post-request that adds new objects to the server
    request_add_car = requests.post(f"{URL}", json=new_car)

    self.enter_model.delete(0, END)
    self.enter_license.delete(0, END)
    self.enter_price.delete(0, END)
    self.enter_manufacturer.delete(0, END)

    if request_add_car.status_code == 200:
        Label(self, text="Added a car", fg="green").grid(row=0, column=1)

        Label(self, text=request_add_car.json(), fg="green").grid(row=7, columnspan=2)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_add_car.json(), fg="red").grid(row=7, columnspan=2)


def Clicked_btn_send_car_edit(self):
    enter_license_edit = self.enter_license_edit.get()
    Model_name_car_edit = self.enter_model_edit.get()
    enter_price_edit = self.enter_price_edit.get()
    enter_manufacturer_edit = self.enter_manufacturer_edit.get()

    edit_car = {
        "license": f"{enter_license_edit}",
        "model": f"{Model_name_car_edit}",
        "producer": f"{enter_manufacturer_edit}",
        "price": enter_price_edit
    }

    # sending a post-request that adds new objects to the server
    request_edit_car = requests.put(f"{URL}", json=edit_car)

    self.enter_license_edit.delete(0, END)
    self.enter_model_edit.delete(0, END)
    self.enter_price_edit.delete(0, END)
    self.enter_manufacturer_edit.delete(0, END)

    if request_edit_car.status_code == 200:
        Label(self, text="Edited a car", fg="green").grid(row=0, column=1)

        Label(self, text=request_edit_car.json(), fg="green").grid(row=8, columnspan=2)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_edit_car.json(), fg="red").grid(row=8, columnspan=2)


def Clicked_btn_send_car_delete(self):
    enter_license_delete = self.enter_license_delete.get()

    delete_car = {
        "license": f"{enter_license_delete}",
    }

    request_delete_car = requests.delete(f"{URL}", json=delete_car)

    if request_delete_car.status_code == 200:
        Label(self, text="Removed a car", fg="green").grid(row=0, column=1)

        Label(self, text=request_delete_car.json(), fg="green").grid(row=7, columnspan=2)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_delete_car.json(), fg="red").grid(row=7, columnspan=2)
