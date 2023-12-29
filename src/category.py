class Category:
    __count_categories = 0
    __count_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        self.__count_categories += 1
        self.__count_products += len(set(product["name"] for product in products))

    @property
    def count_categories(self) -> int:
        return self.__count_categories

    @property
    def count_products(self) -> int:
        return self.__count_products

    @property
    def products(self):
        return "\n".join(
            [
                f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт."
                for product in self.__products
            ]
        )
