import pytest

from src.smartphone import Smartphone


@pytest.fixture
def sm_phone():
    return Smartphone(
        "Samsung Galaxy",
        "256GB, Серый цвет, 200MP камера",
        200000.0,
        8,
        "Qualcomm Snapdragon 8 Gen2",
        "C23 Ultra",
        256,
        "Серый",
    )


def test_create_product(sm_phone):
    assert len(Smartphone.products) == 1
    sm_phone.create_product("Phone", "for content", 15000, 5)
    assert len(Smartphone.products) == 1
    Smartphone("Smartphone", "for game", 30000, 2, "8gb", "gamepad", 256, "black")
    assert len(Smartphone.products) == 2


def test_create_product_raise(sm_phone):
    with pytest.raises(TypeError):
        Smartphone.create_product(1, "2", "3", 4, 5)


def test_init(sm_phone):
    assert sm_phone.color == "Серый"
    assert sm_phone.memory == 256


def test_add(sm_phone):
    sm_phone2 = Smartphone(
        "Samsung Galaxy",
        "256GB, Серый цвет, 200MP камера",
        210000.0,
        5,
        "Qualcomm Snapdragon 8 Gen2",
        "C23 Ultra",
        256,
        "Черный",
    )
    assert sm_phone + sm_phone2 == 2_650_000


def test_add_raise(sm_phone):
    with pytest.raises(TypeError):
        sm_phone + 10
