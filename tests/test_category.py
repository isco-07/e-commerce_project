import pytest

from src.category import Category


@pytest.fixture
def category_obj():
    return Category(
        "Phones",
        "iphone series",
        ["iphone 10", "iphone 11", "iphone 13 Pro Max", "iphone 15 Pro"],
    )


def test_init(category_obj):
    assert category_obj.name == "Phones"
    assert category_obj.description == "iphone series"
    assert category_obj.products == [
        "iphone 10",
        "iphone 11",
        "iphone 13 Pro Max",
        "iphone 15 Pro",
    ]


def test_all_categories(category_obj):
    assert category_obj.all_categories == 1


def test_all_products(category_obj):
    assert category_obj.all_products == 4
