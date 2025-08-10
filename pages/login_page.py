from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from test_data.test_data import TestData


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Page methods
    # def __init__(self, driver):
    #     super().__init__(driver)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # URL of the website
    def open_login_page(self):
        self.open_url(TestData.BASE_URL)

    def enter_username(self):
        self.type_text(self.USERNAME_INPUT, TestData.USERNAME)

    def enter_password(self):
        self.type_text(self.PASSWORD_INPUT, TestData.PASSWORD)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self):
        self.enter_username()
        self.enter_password()
        self.click_login()
