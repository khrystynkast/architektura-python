import pytest
from product import Product


@pytest.fixture
def product():
    return Product("Laptop", 100.0, 10)


def test_is_available(product):
    assert product.is_available() is True


@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (3, 13),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-5)


def test_remove_stock_positive(product):
    product.remove_stock(4)
    assert product.quantity == 6


def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(999)


def test_remove_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(-1)


def test_total_value(product):
    assert product.total_value() == 100.0 * 10


@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),     
    (50, 50.0),     
    (100, 0.0),     
])
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("percent", [-10, -1, 101, 150])
def test_apply_discount_invalid_values(product, percent):
    with pytest.raises(ValueError):
        product.apply_discount(percent)
