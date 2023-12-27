import pytest

from src.category import Category


@pytest.fixture
def category_obj():
    return Category(
        "Phones",
        "iphone series",
        [
            {
                "name": "iphone 10",
                "description": "phone",
                "price": 35000.0,
                "quantity": 4,
            },
            {
                "name": "iphone 11",
                "description": "phone",
                "price": 55000.0,
                "quantity": 14,
            },
        ],
    )


def test_init(category_obj):
    assert category_obj.name == "Phones"
    assert category_obj.description == "iphone series"


def test_all_categories(category_obj):
    assert category_obj.count_categories == 1


def test_all_products(category_obj):
    assert category_obj.count_products == 2


def test_products(category_obj):
    assert category_obj.products == (
        "iphone 10, 35000.0 руб. Остаток: 4 шт.\n"
        "iphone 11, 55000.0 руб. Остаток: 14 шт."
    )
