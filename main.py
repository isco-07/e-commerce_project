from src.category import Category
from src.product import Product
from src.views import read_json

if __name__ == '__main__':
    categories_obj = []
    products_obj = []
    products_list = read_json('products.json')
    for i in products_list:
        categories_obj.append(Category(i['name'], i['description'], i['products']))
        for elem in i['products']:
            products_obj.append(Product(elem['name'], elem['description'], elem['price'],
                                        elem['quantity']))

    print(len(Product.products))
    Product.create_product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 200000.0, 8)
    print(len(Product.products))
    Product.create_product('Samsung Galaxy S21 Ultra 5G', '256GB, Серый цвет, 100MP камера', 160000.0, 8)
    print(len(Product.products))
    print()
    if len(products_obj) > 0:
        new_price = round(float(input("Ведите цену товара: ")), 2)
        if new_price < products_obj[-1].price:
            print(f"Цена товара до предложения снизить цену: {products_obj[-1].price}")
            products_obj[-1].price = new_price
            print(f"Цена товара после принятия решения о снижении цены: {products_obj[-1].price}\n")
        else:
            print(f"Цена товара осталась прежней либо увеличилась: {new_price}\n")

    for category in categories_obj:
        print(category)
    print()
    for product in products_obj:
        print(product)
    print()
    if len(products_obj) > 1:
        print(
            f"Общая сумма последних двух товаров с учетом количества "
            f"каждого товара: {products_obj[-2] + products_obj[-1]}")
