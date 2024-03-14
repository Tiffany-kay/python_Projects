# code to calculate point of sale
from datetime import datetime  # import datetime to calculate duration


class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        pass  # To be implemented in the derived classes


class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price


class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date

    def calculate_value(self):
        remaining_shelf_life = (self.expiry_date - datetime.now()).days
        discount_factor = max(0, remaining_shelf_life / 30)  # Assume a discount based on remaining days
        return self.quantity_in_stock * self.unit_price * (1 - discount_factor)


class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price


# Example usage:
simple_product = SimpleProduct(1, "Widget", 100, 2.5)
perishable_product = PerishableProduct(2, "Fresh Produce", 50, 1.5, datetime(2024, 3, 31))
digital_product = DigitalProduct(3, "Software", 14, 78)

print(simple_product.calculate_value())
print(perishable_product.calculate_value())
print(digital_product.calculate_value())
