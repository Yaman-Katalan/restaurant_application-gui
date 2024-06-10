import pytest
from restaurant_app.main import RestaurantApp
import tkinter as tk

@pytest.fixture
def app():
    root = tk.Tk()
    app = RestaurantApp(root)
    return app

def test_pizza_quantity(app):
    app.pizza_qty.insert(0, "2")
    assert app.pizza_qty.get() == "2"

def test_burger_quantity(app):
    app.burger_qty.insert(0, "3")
    assert app.burger_qty.get() == "3"
