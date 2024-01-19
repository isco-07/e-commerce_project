from src.product import Product


class LawnGrass(Product):
    products = []

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country_of_origin: str,
        germin_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germin_period = germin_period
        self.color = color

    def __repr__(self):
        return (super().__repr__())[
            :-1
        ] + f", {self.country_of_origin}, {self.germin_period}, {self.color})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return super().__add__(other)
        else:
            raise TypeError("Разные товары суммировать нельзя")

    def create_product(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        if isinstance(self, (self.__class__, Product)):
            super().create_product(name, description, price, quantity)
        else:
            raise TypeError(
                "Данный объект не соответствует требованиям создания объектов класса"
            )
