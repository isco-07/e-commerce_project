from src.option import Option
from src.new_object_error import NewObjectError


class Order(Option):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        if quantity > 0:
            self.quantity = quantity
            print("Обработка добавления товара завершена")
            print("Товар добавлен")
        else:
            print("Обработка добавления товара завершена")
            raise NewObjectError
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.quantity}, {self.price})"

    def __str__(self):
        return f"{self.name}: {self.quantity}шт. на общую сумму {self.price * self.quantity}"
