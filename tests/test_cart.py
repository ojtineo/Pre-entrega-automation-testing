from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.reader import reads_productos_json

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage

    driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user","secret_sauce")

    # Leer el primer producto del JSON
    producto = reads_productos_json()[0]

    inventory_page.agregar_producto(producto["nombre"])

    assert inventory_page.obtener_contador_ccarrito() == "1"

    # Ir al carrito
    inventory_page.ir_al_carrito()

    # Validar nombre contra el JSON
    assert cart_page.obtener_nombre_producto() == producto["nombre"]

    # Validar precio contra el JSON
    assert cart_page.obtener_precio_producto() == producto["precio"]