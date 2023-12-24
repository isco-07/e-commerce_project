from src.category import Category
from src.product import Product
from src.views import read_json

if __name__ == '__main__':
    products_list = read_json('products.json')
    for i in products_list:
        category_obj = Category(i['name'], i['description'], i['products'])
        for elem in i['products']:
            product_obj = Product(elem['name'], elem['description'], elem['price'],
                                  elem['quantity'])
