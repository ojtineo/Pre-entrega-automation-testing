import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver =webdriver.Chrome()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {
            "x-api-key": "free_user_3MOmMCfXfsuxIoY1up23TmadcDI"}