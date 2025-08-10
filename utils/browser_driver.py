import os
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from dotenv import load_dotenv

class EnvironmentSetup:
    driver = None

    def initialize_driver(self):
        load_dotenv()  # Load env variables from .env file

        browser = os.getenv("BROWSER", "chrome").lower()
        wait = int(os.getenv("IMPLICIT_WAIT", "10"))
        headless = os.getenv("HEADLESS", "false").lower() == "true"

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
            self.driver = Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            self.driver = Firefox(options=options)


        else:
            raise Exception(f"Invalid browser name '{browser}' provided in environment variables")

        self.driver.maximize_window()
        self.driver.implicitly_wait(wait)
        return self.driver
