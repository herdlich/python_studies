class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def sell(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return

        if amount > self.quantity:
            print("Not enough products")
            return

        self.quantity -= amount


product_one = Product("Product One", 100, 10)
product_two = Product("Product Two", 200, 5)

total_price_one = product_one.total_price()
total_price_two = product_two.total_price()

print("(1) TOTAL PRICE:", total_price_one)
print("(2) TOTAL PRICE:", total_price_two)

print("---------------------")

product_one.sell(5)
print("(1) AFTER THE SALE:", product_one.quantity)

product_two.sell(5)
print("(2) AFTER THE SALE:", product_two.quantity)
