from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests

URL = "http://127.0.0.1:5000/"


# display all the relevant information:

def get_cars_for_textbox(self):
    cars = requests.get(f"{URL}/car")

    text = ScrolledText(self, wrap=WORD, width=40, font=("Times New Roman", 13))
    text.grid(pady=10, padx=10, column=1, rowspan=5)

    insert_list_head = f"license, model, producer,  price, customer_number\n\n"
    text.insert(INSERT, insert_list_head)

    if cars.status_code == 200:
        insert_list_car = cars.json()

        for car in insert_list_car:
            license = car['license']
            model = car['model']
            price = car['price']
            producer = car["producer"]
            customer_number = car['customer_number']

            insert_list_car = f"{license}, {model}, {producer},  {price}, {customer_number} \n"

            text.insert(INSERT, insert_list_car)


def get_customers_for_textbox(self):
    customers = requests.get(f"{URL}/customer")

    text = ScrolledText(self, width=40, relief="groove", wrap=WORD, font=("Times New Roman", 13))
    text.grid(column=1, rowspan=4, padx=10, pady=10)

    insert_list_head = "CustomerNumber, name, lastname, email \n\n"
    text.insert(INSERT, insert_list_head)

    if customers.status_code == 200:
        customer_list = customers.json()

        for car in customer_list:
            CustomerNumber = car['customerNumber']
            name = car['name']
            email = car['email']
            lastname = car['lastname']

            insert_list = f"{CustomerNumber}, {name}, {lastname}, {email}  \n"
            text.insert(END, insert_list)

    else:
        insert_list_none = "No customers \n"
        text.insert(INSERT, insert_list_none)


def get_car_and_customer(self):
    customers = requests.get(f"{URL}/customer")
    cars = requests.get(f"{URL}/car")

    text = ScrolledText(self, width=40, relief="groove", wrap=WORD, font=("Times", 13))
    text.grid(column=1, rowspan=4, padx=10, pady=10)

    if customers.status_code == 200:
        customer_list = customers.json()

        insert_list_head = "CustomerNr, name, lastname, email  \n\n"
        text.insert(END, insert_list_head)

        for car in customer_list:
            CustomerNumber = car['customerNumber']
            name = car['name']
            email = car['email']
            lastname = car['lastname']

            insert_list = f"{CustomerNumber}, {name}, {lastname}, {email}\n"
            text.insert(END, insert_list)

    else:
        insert_list_none = "Error occurred\n"
        text.insert(INSERT, insert_list_none)

    insert_list_car_sep = "\n\n ====================================\n\n"
    text.insert(INSERT, insert_list_car_sep)

    if cars.status_code == 200:
        insert_list_car = cars.json()

        insert_list_car_head = "\n License, Model, producer, Price, Rent \n\n"
        text.insert(INSERT, insert_list_car_head)

        for car in insert_list_car:
            license = car['license']
            model = car['model']
            price = car['price']
            producer = car["producer"]
            customer_number = car['customer_number']

            insert_list_car = f"{license}, {model},{producer}, {price}, {customer_number}\n"
            text.insert(INSERT, insert_list_car)
