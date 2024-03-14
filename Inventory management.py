#  code for an inventory management system
from datetime import datetime, timedelta

class Product:  # declare a class
    def __init__(self, product_id, name, quantity_in_stock):  # class initialization
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

class SimpleProduct(Product): # SimpleProduct inheriting from Product class
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(SimpleProduct):  # PerishableProduct inheriting from SimpleProduct class.
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock, unit_price)
        self.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')

    def calculate_value(self):  # declare method
        total_value = super().calculate_value()
        if self.expiry_date - datetime.now() <= timedelta(days=60):
            return total_value - (0.1 * total_value)
        else:
            return total_value

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

while True:  # User input
    product_id = input("Enter Product ID: ")
    name = input("Enter product name: ")
    quantity_in_stock = int(input("Whats the quantity in stock? "))
    unit_price = float(input("Enter unit price: "))
    expiry_date = input("Enter product's expiry date (YYYY-MM-DD): ")

    simple_product = SimpleProduct(product_id, name, quantity_in_stock, unit_price)
    print("PRODUCT ID = ", product_id)
    print("PRODUCT NAME = ", name)
    print("PRODUCT VALUE = ", simple_product.calculate_value())

    perishable_product = PerishableProduct(product_id, name, quantity_in_stock, unit_price, expiry_date)
    print("DISCOUNT APPLIED = ", perishable_product.calculate_value())

    digital_product = DigitalProduct(product_id, name, quantity_in_stock, unit_price)
    print("DIGITAL PRODUCT VALUE ", digital_product.calculate_value())
    choice = input("Do you want another set of products? (Y/N)")
    if choice.lower() != 'y':
        breakpoint()
