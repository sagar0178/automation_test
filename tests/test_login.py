import time

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.browser_driver import EnvironmentSetup

@pytest.fixture
def driver():
    env_setup = EnvironmentSetup()
    driver = env_setup.initialize_driver()
    if driver is None:
        pytest.skip("Driver initialization failed due to invalid browser setting.")
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()
    print("logged in successfully")
    time.sleep(20)
