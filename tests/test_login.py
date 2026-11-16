from pages.login_page import LoginPage
import pytest

def test_login_exitoso(driver):
    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user","secret_sauce")

    assert "/inventory.html" in driver.current_url