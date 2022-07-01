import csv  # including cvs library

with open('customers.csv', 'r') as csv_file:  # open the file, it automatically closes
    reader = csv.reader(csv_file, skipinitialspace=True)
    # defining a reader that will be used to read data from the file
    next(reader)  # skip the first row
    for row in reader:  # reading data row for row
        id = row[0]  # getting id in the first row
        name = row[1]
        address = row[2]
        print(f'Customer: {name}, {address}')

with open('products.csv') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)
    # Defining the reader as dictionary reader (slightly different in syntax)
    for row in reader:
        id = row['id']
        name = row['name']
        price = row['price']

        print(f'Product: {name}, {price}')

amounts = [0, 0, 0, 0, 0, 0]  # python is stupid
with open('orders.csv') as file1, open('products.csv') as file2:
    reader1 = csv.DictReader(file1, skipinitialspace=True)  # orders
    reader2 = csv.DictReader(file2, skipinitialspace=True)  # products

    for row in reader1:  # go through the list of orders
        a = 0
        amounts.append(a)  # because Python id stupid

        productid = int(row['productid'])
        amount = int(row['amount'])
        amounts[productid - 1] += amount

    for row in reader2:
        id = int(row['id'])
        name = row['name']
        print(f'{name} amount: {amounts[id - 1]}')
        # product id starts with 1 and lists start with 0, therefore we subtract 1

Gross_income = [0, 0, 0, 0, 0, 0]
list_price = [0, 0, 0, 0, 0, 0]
with open('orders.csv') as file1, open('products.csv') as file2:
    reader1 = csv.DictReader(file1, skipinitialspace=True)  # orders
    reader2 = csv.DictReader(file2, skipinitialspace=True)  # products

    for row in reader1:  # go through the orders file
        count = 0
        Gross_income.append(count)
        productid = int(row['productid'])
        amount = int(row['amount'])
        Gross_income[productid - 1] += amount

    for row in reader2:
        Product_id = int(row['id'])
        name = row['name']
        price = int(row['price'])
        print(f'{name} gross income: {Gross_income[Product_id - 1] * price}')

Costumer_spend = [0, 0, 0, 0, 0, 0]
Prices = []
with open('orders.csv') as file1, open('products.csv') as file2, open('customers.csv') as file3:
    reader1 = csv.DictReader(file1, skipinitialspace=True)  # orders
    reader2 = csv.DictReader(file2, skipinitialspace=True)  # products
    reader3 = csv.DictReader(file3, skipinitialspace=True)  # products

    for row in reader2:
        id = int(row['id'])
        price = int(row['price'])
        Prices.append(price)

    for row in reader1:
        count = 0
        Costumer_spend.append(count)
        customerid = int(row['customerid'])
        amount = int(row['amount'])
        productid = int(row['productid'])

        Costumer_spend[customerid - 1] += amount * Prices[productid - 1]

    for row in reader3:
        id = int(row['id'])
        name = row['name']
        print(f'{name} money spent: {Costumer_spend[id - 1]}')
