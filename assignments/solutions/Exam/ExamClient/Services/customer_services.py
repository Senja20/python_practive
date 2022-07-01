from tkinter import *
import requests

URL = "http://127.0.0.1:5000/"


# customer related functions
def Clicked_btn_send_customer_add(self):
    customer_number = self.enter_number.get()
    customer_name = self.enter_name.get()
    customer_name_last = self.enter_name_last.get()
    customer_email = self.enter_email.get()

    new_customer = {
        "customerNumber": f"{customer_number}",
        # has to format them this way so that it can be later send in json format
        "name": f"{customer_name}",
        "lastname": f"{customer_name_last}",
        "email": f"{customer_email}"
    }

    # sending a post-request that adds new objects to the server
    request_add_customer = requests.post(f"{URL}/customer", json=new_customer)

    if request_add_customer.status_code == 200:
        Label(self, text="Customer added", fg="green").grid(row=0, column=1)
        Label(self, text=request_add_customer.json(), fg="green").grid(row=7, columnspan=2)

        self.enter_number.delete(0, END)
        self.enter_name.delete(0, END)
        self.enter_email.delete(0, END)
        self.enter_name_last.delete(0, END)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_add_customer.json(), fg="red").grid(row=7, columnspan=2)


def Clicked_btn_send_customer_edit(self):
    enter_number_edit = self.enter_number_edit.get()
    enter_name_edit = self.enter_name_edit.get()
    enter_email_edit = self.enter_email_edit.get()
    enter_last_name_edit = self.enter_name_last_edit.get()

    edit_customer = {
        "customerNumber": f"{enter_number_edit}",
        "name": f"{enter_name_edit}",
        "lastname": f"{enter_last_name_edit}",
        "email": f"{enter_email_edit}"
    }

    # sending a post-request that adds new objects to the server
    request_edit_car = requests.put(f"{URL}/customer", json=edit_customer)

    if request_edit_car.status_code == 200:
        Label(self, text="Customer edited", fg="green").grid(row=0, column=1)
        Label(self, text=request_edit_car.json(), fg="green").grid(row=7, columnspan=2)

        self.enter_number_edit.delete(0, END)
        self.enter_name_edit.delete(0, END)
        self.enter_email_edit.delete(0, END)
        self.enter_name_last_edit.delete(0, END)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_edit_car.json(), fg="red").grid(row=7, columnspan=2)


def Clicked_btn_send_customer_delete(self):
    enter_number_delete = self.enter_number_delete.get()

    delete_car = {
        "customerNumber": f"{enter_number_delete}"
    }

    request_delete_car = requests.delete(f"{URL}/customer", json=delete_car)

    if request_delete_car.status_code == 200:
        Label(self, text="Customer removed", fg="green").grid(row=0, column=1)
        Label(self, text=request_delete_car.json(), fg="green").grid(row=7, columnspan=2)

        self.enter_number_delete.delete(0, END)
    else:
        Label(self, text="Error", fg="red").grid(row=0, column=1)
        Label(self, text=request_delete_car.json(), fg="red").grid(row=7, columnspan=2)
