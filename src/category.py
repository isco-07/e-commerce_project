from src.new_object_error import NewObjectError
from src.option import Option


class Category(Option):
    __count_categories = 0
    __count_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            if product["quantity"] > 0:
                self.__products.append(product)
                print("Обработка добавления товара завершена")
                print("Товар добавлен")
            else:
                print("Обработка добавления товара завершена")
                raise NewObjectError

        self.__count_categories += 1
        self.__count_products = len(set(product["name"] for product in self.__products))

    def __len__(self) -> int:
        self.__all_quantity = sum(
            [prod_count["quantity"] for prod_count in self.__products]
        )
        return self.__all_quantity

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.__len__()} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.__products})"

    @property
    def count_categories(self) -> int:
        return self.__count_categories

    @property
    def count_products(self) -> int:
        return self.__count_products

    @property
    def products(self) -> str:
        return "\n".join(
            [
                f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."
                for product in self.__products
            ]
        )

    def average_price(self) -> float | int:
        try:
            average_price = sum(
                [product["price"] * product["quantity"] for product in self.__products]
            ) / sum([product["quantity"] for product in self.__products])
            return round(average_price, 2)
        except ZeroDivisionError:
            return 0
