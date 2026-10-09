from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_inventory():
    driver = webdriver.Chrome()

    try:
        driver.get("https://saucedemo.com/")
        
        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        # Validamos el título de la página
        assert driver.title == "Swag Labs"

        # Validamos que hay mas de un producto
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos) > 0

        # Validamos nombre y precio del primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(By. CLASS_NAME,"inventory_item_name").text
        assert nombre == "Sauce Labs Backpack"

        precio = primer_producto.find_element(By.CLASS_NAME,"inventory_item_price").text
        assert precio == "$29.99"

        #Validamos que estén visibles los elementos importantes (botones: menú y fltro)

        menu = driver.find_element(By.ID,"react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element(By.CSS_SELECTOR,"[data-test='product-sort-container']")
        assert filtro.is_displayed()

    finally:
        driver.quit()