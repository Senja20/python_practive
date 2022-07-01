from tkinter import *

from ExamClient.Services.Get_all_items import get_cars_for_textbox, get_customers_for_textbox, get_car_and_customer
from ExamClient.Services.rent_services import Send_relationship_car_customer, Remove_car_customer_relationship
from ExamClient.Services.car_services import Clicked_btn_send_car_add, Clicked_btn_send_car_edit, \
    Clicked_btn_send_car_delete
from ExamClient.Services.customer_services import Clicked_btn_send_customer_add, Clicked_btn_send_customer_edit, \
    Clicked_btn_send_customer_delete


# 25% Integrate the frontend with the backend REST API
# In files above I store function that are sending requests to my serve api

# initializing may Tk application called "Application"
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(MenuPage)
        self.resizable(width=0, height=0)
        self.title('Fevik Bil')
        self.open_frames = list()

        menubar = Menu(self)
        self.configure(menu=menubar)

        file_menu = Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)

    def switch_frame(self, frame_class):  # function that will switch frame any time it is requested
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# Main Page
# This is where the user will start
class MenuPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text='Menu', fg="Black", font=("Times", 20)).grid(row=0, column=0, padx=10, pady=10)

        Button(self, text='Managing Cars', bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2,
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(frame_Car_Manage)). \
            grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text='Managing Customers', bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove", command=lambda: master.switch_frame(frame_Customer_Manage)). \
            grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text='Assign', bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=88, pady=10, relief="groove", command=lambda: master.switch_frame(Car_rent_Manage)). \
            grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text='Quit', bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=100, pady=10, relief="groove", command=self.master.destroy). \
            grid(row=4, column=0, padx=10, pady=10, sticky="ew")


class frame_Car_Manage(Frame):  # 10% Create the view(s) for managing cars (add, edit, remove)
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Car Management Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        get_cars_for_textbox(self)

        Button(self, text="Add a Car", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove", command=lambda: master.switch_frame(frame_add_car)). \
            grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text="Edit a Car", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(frame_edit_car)).grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text="Remove a Car", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(frame_delete_car)).grid(row=3, column=0, padx=10, pady=10,
                                                                           sticky="ew")

        Button(self, text="Go back to main page", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(MenuPage)).grid(row=4, column=0, padx=10, pady=10, sticky="ew")


class frame_Customer_Manage(Frame):  # 10% Create the view(s) for managing customers (add, edit, remove)
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Customer Management Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        get_customers_for_textbox(self)

        Button(self, text="Add a Customer", bd=10, bg="white", fg="black",
               activeforeground="Orange",
               activebackground="blue", font="Andalusia",
               height=2, highlightcolor="purple", justify="right",
               padx=10, pady=10, relief="groove", command=lambda: master.switch_frame(frame_add_customer)). \
            grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text="Edit a Customer", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(frame_edit_customer)).grid(row=2, column=0, padx=10, pady=10,
                                                                              sticky="ew")

        Button(self, text="Remove a Customer", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(frame_delete_customer)).grid(row=3, column=0, padx=10, pady=10,
                                                                                sticky="ew")

        Button(self, text="Go back to main page", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(MenuPage)).grid(row=4, column=0, padx=10, pady=10, sticky="ew")


class Car_rent_Manage(Frame):  # 10% Create the view(s) required to assign a car to a customer, and to unassign it
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Rental", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        get_car_and_customer(self)

        Button(self, text="Rent a Car", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove", command=lambda: master.switch_frame(Add_relationship)). \
            grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        Button(self, text="Return a Car", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(Remove_relationship)).grid(row=2, column=0, padx=10, pady=10,
                                                                              sticky="ew")

        Button(self, text="Go back to main page", bd=10, bg="white", fg="black",
               activeforeground="white",
               activebackground="blue", font="Andalusia",
               height=2, justify="right",
               padx=10, pady=10, relief="groove",
               command=lambda: master.switch_frame(MenuPage)).grid(row=4, column=0, padx=10, pady=10, sticky="ew")


# Car management frames:

class frame_add_car(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Car Management Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="License number").grid(row=2, column=0)
        Label(self, text="Model of the car").grid(row=3, column=0)
        Label(self, text="Manufacturer").grid(row=4, column=0)
        Label(self, text="Price per day of rent").grid(row=5, column=0)

        self.enter_license = Entry(self)
        self.enter_license.grid(row=2, column=1, padx=100, pady=10)

        self.enter_model = Entry(self)
        self.enter_model.grid(row=3, column=1, padx=100, pady=10)

        self.enter_manufacturer = Entry(self)
        self.enter_manufacturer.grid(row=4, column=1, padx=100, pady=10)

        self.enter_price = Entry(self)
        self.enter_price.grid(row=5, column=1, padx=100, pady=10)

        self.btn_send_car_add = Button(self, text="Send", command=self.call_Clicked_btn_send_car_add)
        self.btn_send_car_add.grid(row=6, column=0, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Car_Manage)) \
            .grid(row=6, column=1, padx=100, pady=10)

    def call_Clicked_btn_send_car_add(self):
        Clicked_btn_send_car_add(self)


class frame_edit_car(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Car Edit Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="License plate number").grid(row=3, column=0)
        Label(self, text="Model of the car").grid(row=4, column=0)
        Label(self, text="Manufacturer").grid(row=5, column=0)
        Label(self, text="Price per day of rent").grid(row=6, column=0)

        self.enter_license_edit = Entry(self)
        self.enter_license_edit.grid(row=3, column=1, padx=100, pady=10)

        self.enter_model_edit = Entry(self)
        self.enter_model_edit.grid(row=4, column=1, padx=100, pady=10)

        self.enter_manufacturer_edit = Entry(self)
        self.enter_manufacturer_edit.grid(row=5, column=1, padx=100, pady=10)

        self.enter_price_edit = Entry(self)
        self.enter_price_edit.grid(row=6, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Car_Manage)) \
            .grid(row=7, column=1, padx=100, pady=10)

        self.btn_send_car_edit = Button(self, text="Send", command=self.call_Clicked_btn_send_car_edit)
        self.btn_send_car_edit.grid(row=7, column=0, padx=100, pady=10)

    def call_Clicked_btn_send_car_edit(self):
        Clicked_btn_send_car_edit(self)


class frame_delete_car(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Car Delete Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="License plate number").grid(row=2, column=0)

        self.enter_license_delete = Entry(self)
        self.enter_license_delete.grid(row=2, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Car_Manage)) \
            .grid(row=5, column=1, padx=100, pady=10)

        self.btn_send_car_edit = Button(self, text="Send", command=self.call_Clicked_btn_send_car_delete)
        self.btn_send_car_edit.grid(row=5, column=0, padx=100, pady=10)

    def call_Clicked_btn_send_car_delete(self):
        Clicked_btn_send_car_delete(self)


# Customer management functions
class frame_add_customer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Add Customer Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="Customer Number").grid(row=2, column=0)
        Label(self, text="Name").grid(row=3, column=0)
        Label(self, text="Last Name").grid(row=4, column=0)
        Label(self, text="Email").grid(row=5, column=0)

        self.enter_number = Entry(self)
        self.enter_number.grid(row=2, column=1, padx=100, pady=10)

        self.enter_name = Entry(self)
        self.enter_name.grid(row=3, column=1, padx=100, pady=10)

        self.enter_name_last = Entry(self)
        self.enter_name_last.grid(row=4, column=1, padx=100, pady=10)

        self.enter_email = Entry(self)
        self.enter_email.grid(row=5, column=1, padx=100, pady=10)

        self.btn_send_customer_add = Button(self, text="Send", command=self.call_Clicked_btn_send_customer_add)
        self.btn_send_customer_add.grid(row=6, column=0, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Customer_Manage)) \
            .grid(row=6, column=1, padx=100, pady=10)

    def call_Clicked_btn_send_customer_add(self):
        Clicked_btn_send_customer_add(self)


class frame_edit_customer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Customer Edit Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="customer number").grid(row=2, column=0)
        Label(self, text="Name").grid(row=3, column=0)
        Label(self, text="Last name").grid(row=4, column=0)
        Label(self, text="Email").grid(row=5, column=0)

        self.enter_number_edit = Entry(self)
        self.enter_number_edit.grid(row=2, column=1, padx=100, pady=10)

        self.enter_name_edit = Entry(self)
        self.enter_name_edit.grid(row=3, column=1, padx=100, pady=10)

        self.enter_name_last_edit = Entry(self)
        self.enter_name_last_edit.grid(row=4, column=1, padx=100, pady=10)

        self.enter_email_edit = Entry(self)
        self.enter_email_edit.grid(row=5, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Customer_Manage)) \
            .grid(row=6, column=1, padx=100, pady=10)

        self.btn_send_car_edit = Button(self, text="Send", command=self.call_Clicked_btn_send_customer_edit)
        self.btn_send_car_edit.grid(row=6, column=0, padx=100, pady=10)

    def call_Clicked_btn_send_customer_edit(self):
        Clicked_btn_send_customer_edit(self)


class frame_delete_customer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Customer Delete Menu", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="Customer Number").grid(row=2, column=0)

        self.enter_number_delete = Entry(self)
        self.enter_number_delete.grid(row=2, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(frame_Customer_Manage)) \
            .grid(row=5, column=1, padx=100, pady=10)

        self.btn_send_customer_delete = Button(self, text="Send", command=self.call_Clicked_btn_send_customer_delete)
        self.btn_send_customer_delete.grid(row=5, column=0, padx=100, pady=10)

    def call_Clicked_btn_send_customer_delete(self):
        Clicked_btn_send_customer_delete(self)


class Add_relationship(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Rent a car", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="Customer Number").grid(row=1, column=0)
        Label(self, text="Car license").grid(row=2, column=0)

        self.entry_customer_number_relationship = Entry(self)
        self.entry_customer_number_relationship.grid(row=1, column=1, padx=100, pady=10)

        self.entry_car_license_relationship = Entry(self)
        self.entry_car_license_relationship.grid(row=2, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(Car_rent_Manage)) \
            .grid(row=5, column=1, padx=100, pady=10)

        self.btn_rent_car_to_customer = Button(self, text="Send", command=self.call_Send_relationship_car_customer)
        self.btn_rent_car_to_customer.grid(row=5, column=0, padx=100, pady=10)

    def call_Send_relationship_car_customer(self):
        Send_relationship_car_customer(self)


class Remove_relationship(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Return a car", fg="Black", font=("Times", 20)). \
            grid(row=0, padx=10, pady=10, sticky="ew")

        Label(self, text="Car license").grid(row=2, column=0)

        self.entry_customer_number_relationship = Entry(self)
        self.entry_customer_number_relationship.grid(row=2, column=1, padx=100, pady=10)

        Button(self, text="Return", command=lambda: master.switch_frame(Car_rent_Manage)) \
            .grid(row=5, column=1, padx=100, pady=10)

        self.btn_rent_car_to_customer = Button(self, text="Send", command=self.call_Remove_car_customer_relationship)
        self.btn_rent_car_to_customer.grid(row=5, column=0, padx=100, pady=10)

    def call_Remove_car_customer_relationship(self):
        Remove_car_customer_relationship(self)


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
