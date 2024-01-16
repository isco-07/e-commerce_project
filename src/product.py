from src.mixin import Mixin
from src.shop import Shop


class Product(Shop, Mixin):
    products: list = []

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.products.append(self)

    def __repr__(self):
        return (
            super().__repr__()
            + f"({self.name}, {self.description}, {self.price}, {self.quantity})"
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        return self.__price * self.quantity + other.__price * other.quantity

    @staticmethod
    def create_product(
        name: str, description: str, price: float, quantity: int
    ) -> None:
        for product in Product.products:
            if name == product.name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                break
        else:
            Product(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < self.__price:
            answer = input("Согласны снизить цену? y (значит yes) или n (значит no): ")
            if answer.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price
