import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()
        assert "/inventory.html" in driver.current_url

        logo = driver.find_element(By.CLASS_NAME,"app_logo")
        assert logo.text == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
        driver.quit()

# Agregando una prueba negativa

def test_login_negativo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("Secret_sauce")
        boton_login.click()

        mensaje_error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Epic sadface: Username and password do not match any user in this service" in mensaje_error

    finally:
        driver.quit()
