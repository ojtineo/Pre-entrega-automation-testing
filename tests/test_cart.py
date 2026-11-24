from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.reader import read_products_json
from utils.logger import logger

def test_cart(driver):
    try:
        logger.info("Iniciando prueba del carrito ")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        logger.info("Accesando a la página principal de Saucedemo")
        driver.get("https://www.saucedemo.com/")

        logger.info("Ingresando credenciales para iniciar sesión")
        login_page.login("standard_user","secret_sauce")
        logger.info("Inicio de sesión con usuario correcto:'standard_user'")

        logger.info("Ingresando a la página del inventario")

        logger.info("Leyendo el primer producto del JSON")
        # Leer el primer producto del JSON
        producto = read_products_json()[0]
        print(producto)

        logger.info("Agregando producto del JSON al carrito")
        inventory_page.agregar_producto(producto["nombre"])

        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Prueba del contador del carrito validada")

        logger.info("Ir a la página del carrito")
        # Ir al carrito
        inventory_page.ir_al_carrito()

        # Validar nombre contra el JSON
        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Prueba del nombre del producto en carrito contra el JSON validada")

        # Validar precio contra el JSON
        assert cart_page.obtener_precio_producto() == producto["precio"]
        logger.info("Prueba del precio del producto en carrito contra el JSON validada")
    except Exception:
        logger.info("Error durante la prueba del carrito")
    
