from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Iniciando prueba de inventario")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Accesando a la página principal de Saucedemo")
        driver.get("https://www.saucedemo.com/")

        logger.info("Ingresando credenciales para iniciar sesión")
        login_page.login("standard_user","secret_sauce")
        logger.info("Inicio de sesión con usuario correcto:'standard_user'")

        productos = inventory_page.obtener_productos()
        logger.info("Productos obtenidos del inventario")

        assert len(productos) > 0
        logger.info("Cantidad de productos encontrados verificados")

        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        logger.info("Verificando nombre del primer producto: 'Sauce Labs Backpack'")
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Verificando precio del primer producto: '$29.99'")

        assert inventory_page.menu_visible()
        logger.info("Verificando visibilidad del menú")
        assert inventory_page.filtro_visible()
        logger.info("Verificando visibilidad del filtro de productos")
    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise
    