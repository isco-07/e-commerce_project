from src.product import Product


class Smartphone(Product):
    products = []

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        cpu: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.cpu = cpu
        self.model = model
        self.memory = memory
        self.color = color
        # Smartphone.products.append(self)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return super().__add__(other)
        else:
            raise TypeError("Разные товары суммировать нельзя")

    def create_product(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        if isinstance(self, (self.__class__, Product)):
            super().create_product(name, description, price, quantity)
        else:
            raise TypeError(
                "Данный объект не соответствует требованиям создания объектов класса"
            )
