from src.product import Product


def test_create_product():
    product_obj1 = Product("iphone 11", "for calls", 59990.00, 5)
    assert len(product_obj1.products) == 1
    Product.create_product("iphone 11", "for calls", 59990.00, 5)
    assert len(product_obj1.products) == 1
    Product.create_product("iphone 12", "for games", 59990.00, 5)
    assert len(product_obj1.products) == 2
    Product.create_product("iphone 11", "for calls", 59990.00, 5)
    assert len(product_obj1.products) == 2


def test_init():
    product_obj = Product("iphone 11", "for calls", 59990.00, 5)
    assert product_obj.name == "iphone 11"
    assert product_obj.description == "for calls"
    assert product_obj.quantity == 5


def test_price():
    product_obj = Product("iphone 11", "for calls", 59990.00, 5)
    assert product_obj.price == 59990.00
    product_obj.price = 62000.00
    assert product_obj.price == 62000.00


def test_str():
    product_obj = Product("iphone 11", "for calls", 59990.00, 5)
    assert str(product_obj) == "iphone 11, 59990.0 руб. Остаток: 5 шт."


def test_add():
    product_obj1 = Product("iphone 11", "for calls", 59990.00, 5)
    product_obj2 = Product("iphone 12", "for games", 59990.00, 5)
    assert product_obj1 + product_obj2 == 599900.0
