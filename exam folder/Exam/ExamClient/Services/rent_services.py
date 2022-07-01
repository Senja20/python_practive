from tkinter import *
import requests

URL = "http://127.0.0.1:5000/"


# relationship and rent related functions
def Send_relationship_car_customer(self):
    car_rel = self.entry_car_license_relationship.get()
    customer_rel = self.entry_customer_number_relationship.get()

    car_rent = {
        "customerNumber": f"{customer_rel}",
        "license": f"{car_rel}"
    }

    request_create_relationship = requests.post(f"{URL}/rent", json=car_rent)

    if request_create_relationship.status_code == 200:
        Label(self, text="Car rented", fg="green").grid(row=0, column=1)

        Label(self, text=request_create_relationship.json(), fg="green").grid(row=6, columnspan=2, column=0)

        self.entry_car_license_relationship.delete(0, END)
        self.entry_customer_number_relationship.delete(0, END)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_create_relationship.json(), fg="red").grid(row=6, columnspan=2, column=0)


def Remove_car_customer_relationship(self):
    car_return = self.entry_customer_number_relationship.get()

    return_car = {
        "license": f"{car_return}"
    }

    request_create_relation = requests.put(f"{URL}/rent", json=return_car)

    if request_create_relation.status_code == 200:
        Label(self, text="Car returned", fg="green").grid(row=0, column=1)
        Label(self, text=request_create_relation.json(), fg="green").grid(row=6, column=0, columnspan=2)

        self.entry_customer_number_relationship.delete(0, END)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_create_relation.json(), fg="red").grid(row=6, column=0, columnspan=2)
