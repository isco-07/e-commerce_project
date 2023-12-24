class Category:
    name: str
    description: str
    products: list

    __all_categories = 0
    __all_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.__all_categories += 1
        self.__all_products += len(products)

    @property
    def all_categories(self):
        return self.__all_categories

    @property
    def all_products(self):
        return self.__all_products
