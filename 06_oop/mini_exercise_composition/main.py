class Product:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self):
        return self.name


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Product must be of type Product")

        self.products.append(product)

    def remove_product(self, name: str) -> None:
        if name not in self.products:
            raise RuntimeError(f'Product {name} not in shopping cart')

        self.products.remove(name)

    def get_products(self) -> list:
        return self.products
