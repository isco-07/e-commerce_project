import pytest

from src.product import Product


@pytest.fixture
def product_obj():
    return Product("iphone 11", "for calls", 59990.00, 5)


def test_init(product_obj):
    assert product_obj.name == "iphone 11"
    assert product_obj.description == "for calls"
    assert product_obj.quantity == 5


def test_price(product_obj):
    assert product_obj.price == 59990.00
    product_obj.price = 62000.00
    assert product_obj.price == 62000.00


def test_create_product(product_obj):
    assert len(product_obj.products) == 1
    Product.create_product("iphone 11", "for calls", 59990.00, 5)
    assert len(product_obj.products) == 1
    Product.create_product("iphone 12", "for games", 59990.00, 5)
    assert len(product_obj.products) == 2
    Product.create_product("iphone 11", "for calls", 59990.00, 5)
    assert len(product_obj.products) == 2

