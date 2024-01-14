import pytest

from src.lawn_grass import LawnGrass


@pytest.fixture
def grass():
    return LawnGrass(
        "Газон",
        "Зеленый газон ГАЗОНCITY, 0.5 кг",
        198,
        42,
        "Россия",
        "25 дней",
        "зеленый",
    )


def test_create_product(grass):
    assert len(LawnGrass.products) == 1
    grass.create_product("grass", "for lawn", 150, 20)
    assert len(LawnGrass.products) == 1


def test_create_product_raise(grass):
    with pytest.raises(TypeError):
        grass.create_product(1, "2", "3", 4, 5)


def test_init(grass):
    assert grass.color == "зеленый"
    assert grass.country_of_origin == "Россия"


def test_add(grass):
    grass2 = LawnGrass(
        "grass",
        "for lawn",
        210.0,
        50,
        "Russia",
        "25 days",
        "green",
    )
    assert grass + grass2 == 18816


def test_add_raise(grass):
    with pytest.raises(TypeError):
        grass + 10
